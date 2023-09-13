import json, time
from django.db.models import Q
from django.core.serializers import serialize
from django.db.models import Count, F

from .Objetos.CursoOBJ import CursoOBJ
from .Objetos.SalonesOBJ import SalonesOBJ
from .Objetos.DocenteOBJ import DocenteOBJ
from .models import AlumnosCursos, DocentesCursos, Docentes, Cursos, Salones, Periodos, Horarios, HorarioCursos, \
    CursosSalones


class ArbolDecision:
    def __init__(self):
        pass

    def simular(self):
        semestre = 1
        ciclo = 2023
        cantMinima = 12
        edificioId = 1
        nombreHorario = "Mi Horario prueba"

        prioridadPorSemestre = False
        prioridadPorDemanda = False
        prioridadPorSemestreActual = True

        elegirSalonExclusivo = True

        # 1 verifica cursos Pre-asignados
        lista_Cursos_Pre_Asignados = self.cursos_preasignados(semestre, ciclo)

        # 2 verifica que cursos cumplen con minimo de estudiantes
        lista_Cursos_Min_Estudiantes = self.cantidad_minima_curso(lista_Cursos_Pre_Asignados, cantMinima)

        # 3 obtiene los docentes postulados para cada curso segun cursos con minimo de apertura
        listaCursosConDocentes = self.verificar_cursos_docentes_aptos(lista_Cursos_Min_Estudiantes)

        # 4 Obtener Salones segun tipo de edificio
        listaSalones = self.getSalonesEdificio(edificioId)

        # 5 Periodos de clase disponibles segun Edificio
        listaPeriodosClase = self.periodosClases(edificioId)

        # 6 Ordenar cursos segun prioridad
        listaCursosOrdenada = self.ordenarPorPiroridad(lista_Cursos_Min_Estudiantes, prioridadPorSemestre,
                                                       prioridadPorDemanda, prioridadPorSemestreActual, semestre)

        # 7 simularAsignacionCursos(lista_Cursos_Min_Estudiantes,listaCursosConDocentes,listaSalones)
        horario_id = self.simularAsignacionCursos(semestre, listaCursosOrdenada, listaCursosConDocentes,
                                                  listaSalones, nombreHorario, listaPeriodosClase, elegirSalonExclusivo)

        return json.dumps({"data": horario_id})

    '''
    Step 1 
    Consultar cursos asignados en PRE-ASIGNACION
    '''

    def cursos_preasignados(self, semestre, ciclo):
        consulta = AlumnosCursos.objects.values('curso_id', 'curso__nombre_curso', 'curso__duracion_periodo',
                                                'semestre', 'ciclo',
                                                'curso__numero_semestre').annotate(
            cantidad_registros=Count('*')).filter(semestre=semestre, ciclo=ciclo).order_by('-cantidad_registros')
        data_json = '{'
        listaCursos = []
        print("CURSOS PRE-ASIGNADOS");
        for resultado in consulta:
            curso = CursoOBJ(resultado['curso_id'], resultado['curso__nombre_curso'], resultado['cantidad_registros'],
                             resultado['curso__numero_semestre'], resultado['curso__duracion_periodo'])
            listaCursos.append(curso)

            # data_json+=json.dumps(curso.to_dict())

            data_json += 'curso_id: ' + str(resultado['curso_id']) + ' '
            data_json += 'nombre_curso: ' + str(resultado['curso__nombre_curso']) + ' '
            data_json += 'cantidad_registros: ' + str(resultado['cantidad_registros']) + ' '

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

    def cantidad_minima_curso(self, listaCursosPosibles, CantMinima):
        listaCursos = []
        for curso in listaCursosPosibles:
            if curso.cantidad_asignados > CantMinima:
                listaCursos.append(curso)
                # print(curso)
                # listaCursos.pop(curso)
            else:
                pass
                # print(" NO CUMPLE: ",curso)
        # self.verificar_cursos_docentes_aptos()
        return listaCursos

    '''
    Step 3
    Metodo para verificar que docentes son aptos para
    impartir cursos pre-asignados
    Return: lista de cursos con los docentes capaces
    '''

    def verificar_cursos_docentes_aptos(self, lista_Cursos_Min_Estudiantes):

        cursos_con_docentes = []
        cursos_con_docentesOBJ = []
        cursos = Cursos.objects.all()

        for curso in cursos:
            docentes_relacionados = DocentesCursos.objects.filter(curso=curso)

            docentes_array = [
                {"id": docente.docente.id,
                 "nombre": docente.docente.nombre,
                 "apellido": docente.docente.apellido,
                 "horario_entrada": docente.docente.horario_entrada.strftime("%H:%M:%S"),
                 "horario_salida": docente.docente.horario_salida.strftime("%H:%M:%S"),
                 "titular": docente.titular}
                for docente in docentes_relacionados
            ]

            curso_con_docente = {
                "curso_id": curso.id_curso,
                "nombre_curso": curso.nombre_curso,
                "numero_semestre": curso.numero_semestre,
                "duracion_periodo": curso.duracion_periodo,
                "docentes": docentes_array
            }
            cursos_con_docentes.append(curso_con_docente)

        for item in cursos_con_docentes:
            curso = CursoOBJ(item['curso_id'], item['nombre_curso'], "", item['numero_semestre'],
                             item["duracion_periodo"])
            for docente in item['docentes']:
                # self, id, nombre, apellido, horario_entrada, horario_salida, titular
                docente = DocenteOBJ(docente["id"], docente["nombre"], docente["apellido"], docente["horario_entrada"],
                                     docente["horario_salida"], docente["titular"])
                # curso.agregar_docente(item['docentes'])
                curso.agregar_docente(docente)
            cursos_con_docentesOBJ.append(curso)

        return cursos_con_docentesOBJ

    def getSalonesEdificio(self, idEdificio):
        salones = Salones.objects.filter(edificio_id=idEdificio,disponible=1)
        lst_salones_OBJ = []
        for item in salones:
            salones_obj = SalonesOBJ(item.id, item.nombre, item.capacidad, item.tipo_mobiliario, item.disponible)
            print(item.id)
            lst_salones_OBJ.append(salones_obj)
        return lst_salones_OBJ

    def getSalonesExclusvos(self, curso_id):
        salonesTmp = CursosSalones.objects.values("salon__id", "salon__nombre", "salon__capacidad",
                                                  "salon__disponible", "salon__tipo_mobiliario",
                                                  "curso__id_curso", "curso__nombre_curso") \
            .filter(curso_id=curso_id, salon__disponible=1)

        lst_salones_OBJ = []
        for item in salonesTmp:
            salones_obj = SalonesOBJ(item["salon__id"], item["salon__nombre"], item["salon__capacidad"],
                                     item["salon__tipo_mobiliario"], item["salon__disponible"])
            lst_salones_OBJ.append(salones_obj)
        return lst_salones_OBJ

    def Existe_Curso_en_Cursos_Salones(self, salon_id, curso_id):
        flag = False
        salonesTmp = CursosSalones.objects.values("salon__id", "salon__nombre", "salon__capacidad",
                                                  "salon__disponible", "salon__tipo_mobiliario","curso__id_curso") \
            .filter(salon_id=salon_id, salon__disponible=1)

        if len(salonesTmp) >= 1:

            for item in salonesTmp:
                #print("Analiza: salon"+str(salon_id)+"=>>"+str(item["curso__id_curso"])+"=="+str(curso_id))
                #print("FALSE")
                if item["curso__id_curso"] == curso_id:
                    return False
            return True

        else:
            print("NO HAY NADA EN EL SALON_ID en reservados CURSOS-SALONES/*/*/*/*"+str(salon_id))
            return False

    def periodosClases(self,edificio_id):
        periodosClase = Periodos.objects.filter(edificio_id=edificio_id)
        return periodosClase

    def ordenarPorPiroridad(self, lista_Cursos_Min_Estudiantes, prioridadPorSemestre, prioridadPorDemanda,
                            prioridadPorSemestreActual, semestre):
        cursos_ordenados = []
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

    def simularAsignacionCursos(self, semestre, cursosOrdenadosPorPrioridad, listaCursosConDocentes, listaSalones,
                                nombreHorario,
                                listaPeriodosClase, elegirSalonExclusivo):

        # guardar nombre del horario(Simulacion)
        horario = Horarios()
        horario.nombre = nombreHorario
        horario.save()
        horarioCurso = HorarioCursos()

        '''
        Logica de Salones
        '''
        # 1 Buscar Salon optimo para cursos
        for curso in cursosOrdenadosPorPrioridad:
            print("ID: " + str(curso.curso_id) + "Nombre: " + curso.nombre_curso + " Semestre: " + str(
                curso.numero_semestre) + " Asignados: " + str(
                curso.cantidad_asignados) + " Duracion_Periodos: " + str(curso.duracion_periodo))

            salones = []
            haySalonExclusivo = False
            periodoLibreInicioId = 0
            periodoLibreFinId = 0
            salonLibreId = 0
            # 2 Buscar si el curso tiene un salon especial
            if (elegirSalonExclusivo == True):
                print("     Salon exclusivo activado")
                salonesTmp = self.getSalonesExclusvos(curso.curso_id)

                if len(salonesTmp) == 0:
                    print("     salonesTmp ==0")
                    salones = listaSalones;

                for aula in salonesTmp:

                    if len(salonesTmp) > 0:
                        print("     TIENE exclusivo---")
                        haySalonExclusivo = True
                        aulaTmp = SalonesOBJ(aula.id, aula.nombre, aula.capacidad,
                                             aula.tipo_mobiliario, aula.disponible)
                        aulaTmp.disponible = aula.disponible
                        salones.append(aulaTmp)
                    else:
                        print("     NO TIENE exclusivo---")
                        haySalonExclusivo = False


            else:
                print("     Salon exclusivo descativado")
                print("Entra en else " + str(len(salones)))
                salones = listaSalones;

            # 3 Verificar que el Salon Este disponible en el horario
            print("Cantidad de salones: " + str(len(salones)))
            periodoLibreInicioId, periodoLibreFinId, salonLibreId = self.buscarHorarioSalon(listaPeriodosClase, salones,
                                                                                            horario, curso)

            id_docente_disponible = self.buscarDocente(listaCursosConDocentes, curso, periodoLibreInicioId, horario.id)
            if id_docente_disponible == None:
                id_docente_disponible = None
            if salonLibreId != 0:

                self.guardarHorarioSalonCursoDocente(horario.id, curso.curso_id, id_docente_disponible, salonLibreId,
                                                     "A", periodoLibreInicioId, periodoLibreFinId)
                print("Termina de evaluar el curso... \n\n\n")
            else:
                print("No se pudo asignar")

        return horario.id

    def buscarDocente(self, listaCursosConDocentes, curso, periodoidCurso, horarioId):
        print("Entra a buscar Docente")
        print(f" Entra en ID: {curso.curso_id} curso: {curso.nombre_curso}")
        for cursoItem in listaCursosConDocentes:

            if cursoItem.curso_id == curso.curso_id:

                # Analiza si tiene docentes
                cantidadDocentes = len(cursoItem.docentes)

                if cantidadDocentes > 0:

                    for docente in cursoItem.docentes:
                        # verifica que este disponible
                        docenteDisponible = self.verificaDocenteDisponible(docente, periodoidCurso, horarioId,
                                                                           curso.duracion_periodo)
                        if docenteDisponible:
                            return docente.id


                else:
                    # No tiene ningun docente
                    return None

    def verificaDocenteDisponible(self, docente, periodoidCurso, horarioId, duracion_curso):

        horarioTMP = HorarioCursos.objects.values("salon__id", "curso__nombre_curso",
                                                  "curso__numero_semestre"). \
            filter(Q(periodo_inicio__gte=periodoidCurso, periodo_fin__lte=(periodoidCurso + duracion_curso)),
                   horario_id=horarioId, salon_id=periodoidCurso, docente_id=docente.id)

        if len(horarioTMP) == 0:
            print("El DOCENTE TIENE LIBRE A ESA HORA :)")
            return True
        else:
            print("Esta ocupado...")
            return False

    def buscarHorarioSalon(self, listaPeriodosClase, salones, horario, curso):
        periodoLibreInicioId = 0
        periodoLibreFinId = 0
        salonLibreId = 0

        for salonItem in salones:

            if self.Existe_Curso_en_Cursos_Salones(salonItem.id, curso.curso_id):
                print("Continue: salon:"+str(salonItem.id)+" curso:"+str(curso.curso_id)+" Nombre "+curso.nombre_curso)
                continue

            else:
                pass

            flagSalon = False

            # verifica que los periodos el salon este diponible
            print("Entra1-----------")
            for periodo in listaPeriodosClase:
                print("Entra2-----------")
                horarioTMP = HorarioCursos.objects.values("salon__id", "curso__nombre_curso",
                                                          "curso__numero_semestre"). \
                    filter(Q(periodo_inicio__gte=periodo.id, periodo_fin__lte=(periodo.id + (curso.duracion_periodo-1))),
                           horario_id=horario.id, salon_id=salonItem.id)

                # time.sleep(0.009)
                if len(horarioTMP) == 0:
                    print("Hay libre")
                    periodoLibreInicioId = periodo.id

                    periodoLibreFinId = (periodo.id + curso.duracion_periodo - 1)
                    salonLibreId = salonItem.id
                    flagSalon = True
                    break
                else:
                    periodoLibreInicioId = 0
                    print("NO HAY LIBRE: ")
                    print("Salon: " + str(salonItem.id) + " Periodo Inicio: " + str(
                        periodo.id) + " Periodo Fin: " + str(periodo.id + curso.duracion_periodo - 1))

            if flagSalon:
                break
        return periodoLibreInicioId, periodoLibreFinId, salonLibreId

    def guardarHorarioSalonCursoDocente(self, horario_id, curso_id, docente_id, salon_id, seccion,
                                        periodo_inicio, periodo_fin):
        print("Guardando horario")
        print("horario_id:", horario_id)
        print("curso_id:", curso_id)
        print("docente_id:", docente_id)
        print("salon_id:", salon_id)
        print("seccion:", seccion)
        print("periodo_inicio:", periodo_inicio)
        print("periodo_fin:", periodo_fin)

        horario_curso_salon_docente = HorarioCursos()
        horario_curso_salon_docente.horario_id = horario_id
        horario_curso_salon_docente.curso_id = curso_id
        horario_curso_salon_docente.docente_id = docente_id
        horario_curso_salon_docente.salon_id = salon_id
        horario_curso_salon_docente.seccion = seccion
        horario_curso_salon_docente.periodo_inicio_id = periodo_inicio
        horario_curso_salon_docente.periodo_fin_id = periodo_fin

        horario_curso_salon_docente.save()
