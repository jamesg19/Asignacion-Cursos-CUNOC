import json
from django.core.serializers import serialize
from django.db.models import Count, F

from .Objetos.CursoOBJ import CursoOBJ
from .models import AlumnosCursos, DocentesCursos, Docentes, Cursos, Salones, Periodos, Horarios

class ArbolDecision:
    def __init__(self):
        pass

    def simular(self):
        semestre=1
        ciclo=2023
        cantMinima=12
        edificioId=1
        nombreHorario="Mi Horario prueba"

        prioridadPorSemestre=False
        prioridadPorDemanda=False
        prioridadPorSemestreActual=True

        #1 verifica cursos Pre-asignados
        lista_Cursos_Pre_Asignados=self.cursos_preasignados(semestre,ciclo)

        #2 verifica que cursos cumplen con minimo de estudiantes
        lista_Cursos_Min_Estudiantes=self.cantidad_minima_curso(lista_Cursos_Pre_Asignados,cantMinima)

        #3 obtiene los docentes postulados para cada curso segun cursos con minimo de apertura
        listaCursosConDocentes=self.verificar_cursos_docentes_aptos(lista_Cursos_Min_Estudiantes)

        #4 Obtener Salones segun tipo de edificio
        listaSalones=self.getSalonesEdificio(edificioId)

        #5 Periodos de clase disponibles segun Edificio
        listaPeriodosClase=self.periodosClases()

        #6 Ordenar cursos segun prioridad
        listaCursosOrdenada=self.ordenarPorPiroridad(lista_Cursos_Min_Estudiantes,prioridadPorSemestre,prioridadPorDemanda,prioridadPorSemestreActual,semestre)

        #7 simularAsignacionCursos(lista_Cursos_Min_Estudiantes,listaCursosConDocentes,listaSalones)
        self.simularAsignacionCursos(semestre,listaCursosOrdenada, listaCursosConDocentes,
                                     listaSalones,nombreHorario,listaPeriodosClase)



        return json.dumps({"data":"OK"})
    '''
    Step 1 
    Consultar cursos asignados en PRE-ASIGNACION
    '''
    def cursos_preasignados(self,semestre, ciclo):
        consulta = AlumnosCursos.objects.values('curso_id', 'curso__nombre_curso', 'semestre', 'ciclo','curso__numero_semestre').annotate(
            cantidad_registros=Count('*')).filter(semestre=semestre, ciclo=ciclo).order_by('-cantidad_registros')
        data_json = '{'
        listaCursos=[]
        print("CURSOS PRE-ASIGNADOS");
        for resultado in consulta:

            curso=CursoOBJ(resultado['curso_id'],resultado['curso__nombre_curso'],resultado['cantidad_registros'], resultado['curso__numero_semestre'])
            listaCursos.append(curso)

            #data_json+=json.dumps(curso.to_dict())

            data_json += 'curso_id: ' + str(resultado['curso_id'])+' '
            data_json += 'nombre_curso: ' + str(resultado['curso__nombre_curso'])+ ' '
            data_json += 'cantidad_registros: ' + str(resultado['cantidad_registros'])+' '

            '''print(resultado['curso_id'], "-", resultado['curso__nombre_curso'], "-",
                  resultado['cantidad_registros'])'''
        data_json += '}'
        ##self.cantidad_minima_curso(listaCursos)
        ##self.verificar_cursos_docentes_aptos(consulta)
        return listaCursos

    '''
    Step 2 
    Verificar Cantidad Minima para apertura de un curso
    Return: Lista de cursos mayores al minimo de apertura de curso
    '''
    def cantidad_minima_curso(self, listaCursosPosibles,CantMinima):
        listaCursos = []
        for curso in listaCursosPosibles:
            if curso.cantidad_asignados> CantMinima:
                listaCursos.append(curso)
                #print(curso)
                #listaCursos.pop(curso)
            else:
                pass
                #print(" NO CUMPLE: ",curso)
        #self.verificar_cursos_docentes_aptos()
        return listaCursos

    '''
    Step 3
    Metodo para verificar que docentes son aptos para
    impartir cursos pre-asignados
    Return: lista de cursos con los docentes capaces
    '''
    def verificar_cursos_docentes_aptos(self,lista_Cursos_Min_Estudiantes):

        cursos_con_docentes = []
        cursos = Cursos.objects.all()

        for curso in cursos:
            docentes_relacionados = DocentesCursos.objects.filter(curso=curso)

            docentes_array = [
                {"id": docente.docente.id,
                 "nombre": docente.docente.nombre,
                 "apellido": docente.docente.apellido,
                 "horario_entrada": docente.docente.horario_entrada.strftime("%H:%M:%S"),
                 "horario_salida":docente.docente.horario_salida.strftime("%H:%M:%S"),
                 "titular":docente.titular}
                 for docente in docentes_relacionados
            ]

            curso_con_docente = {
                "curso_id": curso.id_curso,
                "nombre_curso": curso.nombre_curso,
                "numero_semestre": curso.numero_semestre,
                "docentes": docentes_array
            }
            cursos_con_docentes.append(curso_con_docente)

        for item in cursos_con_docentes:
            curso = CursoOBJ(item['curso_id'],item['nombre_curso'],"",item['numero_semestre'])
            curso.agregar_docente(item['docentes'])

        return cursos_con_docentes


    def getSalonesEdificio(self, idEdificio):
        salones=Salones.objects.filter(edificio_id=idEdificio)
        return salones

    def periodosClases(self):
        periodosClase=Periodos.objects.filter(edificio_id=1)
        return periodosClase

    def ordenarPorPiroridad(self,lista_Cursos_Min_Estudiantes,prioridadPorSemestre,prioridadPorDemanda,prioridadPorSemestreActual,semestre):
        cursos_ordenados=[]
        if (prioridadPorSemestre == True):
            cursos_ordenados = sorted(lista_Cursos_Min_Estudiantes, key=lambda curso: (curso.numero_semestre))

        elif (prioridadPorDemanda):
            cursos_ordenados = sorted(lista_Cursos_Min_Estudiantes, key=lambda curso: (curso.cantidad_asignados),
                                      reverse=True)

        elif (prioridadPorSemestreActual):

            if semestre % 2 != 0:

                cursos_ordenados = sorted(lista_Cursos_Min_Estudiantes,
                                          key=lambda curso: (curso.numero_semestre % 2 == 0, curso.numero_semestre))
            else:
                cursos_ordenados = sorted(lista_Cursos_Min_Estudiantes,
                                          key=lambda curso: (curso.numero_semestre % 2, curso.numero_semestre))
        return cursos_ordenados

    def simularAsignacionCursos(self,semestre,cursosOrdenadosPorPrioridad, listaCursosConDocentes, listaSalones,nombreHorario,
                                listaPeriodosClase):

        #guardar nombre del horario(Simulacion)
        horario=Horarios()
        horario.nombre=nombreHorario
        horario.save()




        #Ordenar cursos segun su semestre Priodidad
        for curso in cursosOrdenadosPorPrioridad:
            print("Nombre: " +curso.nombre_curso+ " Semestre: "+ str(curso.numero_semestre))




