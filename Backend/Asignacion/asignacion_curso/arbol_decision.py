import json
from django.core.serializers import serialize
from django.db.models import Count, F
from .models import AlumnosCursos, DocentesCursos, Docentes, Cursos

class ArbolDecision:
    def __init__(self):
        pass

    # 1 Consultar cursos asignados en PRE-ASIGNACION
    def cursos_preasignados(self):
        consulta = AlumnosCursos.objects.values('curso_id', 'curso__nombre_curso', 'semestre', 'ciclo').annotate(
            cantidad_registros=Count('*')).order_by('-cantidad_registros')
        data_json = ""

        for resultado in consulta:
            data_json += "curso_id:" + json.dumps(resultado['curso_id'])
            data_json += "cantidad_registros:" + json.dumps(resultado['cantidad_registros'])
            print(resultado['curso_id'], "-", resultado['curso__nombre_curso'], "-",
                  resultado['cantidad_registros'])
        #self.cantidad_minima_curso(consulta)
        self.verificar_cursos_docentes_aptos(consulta)
        return data_json

    '''2 Verificar Cantidad Minima para apertura de un curso
    def cantidad_minima_curso(self, listaCursosPosibles):
        listaCursos = []
        for curso in listaCursosPosibles:
            if curso['cantidad_registros'] > 22:
                listaCursos.append(curso)
                #print(curso)
                #listaCursos.pop(curso)
            else:
                pass
                #print(" NO CUMPLE: ",curso)
        self.verificar_cursos_docentes_aptos()
    '''
    '''
    Metodo para verificar que docentes son aptos para
    impartir cursos
    '''
    def verificar_cursos_docentes_aptos(self,listCursosPreasignados):
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
                "docentes": docentes_array
            }
            cursos_con_docentes.append(curso_con_docente)
        print(cursos_con_docentes)

