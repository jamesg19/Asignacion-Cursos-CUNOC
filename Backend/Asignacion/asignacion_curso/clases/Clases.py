class Docente:
    def __init__(self, id, nombre,apellido, horario_entrada,horario_salida):
        self.id = id
        self.nombre = nombre
        self.apellido=apellido
        self.horario_entrada = horario_entrada
        self.horario_salida=horario_salida

class Curso:
    def __init__(self, curso_id, nombre_curso,duracion_periodo,numero_semestre, docentes=[]):
        self.curso_id = curso_id
        self.nombre_curso = nombre_curso
        self.duracion_periodo=duracion_periodo
        self.numero_semestre=numero_semestre
        self.docentes = docentes

