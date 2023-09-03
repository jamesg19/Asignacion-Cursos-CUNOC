
class CursoOBJ:
    def __init__(self, curso_id, nombre_curso,cantidad_asignados,numero_semestre):
        self.curso_id = curso_id
        self.nombre_curso = nombre_curso
        self.docentes = []  # Inicializamos una lista vacía para almacenar docentes
        self.cantidad_asignados=cantidad_asignados
        self.numero_semestre=numero_semestre


    def to_dict(self):
        return {
            'curso_id': self.curso_id,
            'nombre_curso': self.nombre_curso,
            'cantidad_asignados': self.cantidad_asignados,
            'docentes': [docente.to_dict() for docente in self.docentes]
        }
    def agregar_docente(self, docente):
        self.docentes.append(docente)

    def mostrar_docentes(self):
        for docente in self.docentes:
            print(f"Docente ID: {docente.id}")
            print(f"Nombre: {docente.nombre} {docente.apellido}")
            print(f"Horario de entrada: {docente.horario_entrada}")
            print(f"Horario de salida: {docente.horario_salida}")
            print(f"Titular: {'Sí' if docente.titular == 1 else 'No'}")

    def agregarDocentes(self,docente):
        self.docentes.append(docente)

    def mostrarCursosyDocentes(self):
        print(f" Curso id: {self.curso_id}, Nombre: {self.nombre_curso}, cantidad_asignados: {'0' if (self.cantidad_asignados == 0 or self.cantidad_asignados is None) else f'{self.cantidad_asignados}'}");
        self.mostrar_docentes()
'''
# Crear docentes
docente1 = Docente(35096, 'Jorge', 'Aparicio', '16:00:00', '20:00:00', 0)
docente2 = Docente(12345, 'María', 'López', '14:00:00', '18:00:00', 1)

# Crear un curso
curso1 = Curso(28, 'Social Humanística 1')

# Agregar docentes al curso
curso1.agregar_docente(docente1)
curso1.agregar_docente(docente2)

# Mostrar docentes del curso
print(f"Información del curso {curso1.nombre_curso}:")
curso1.mostrar_docentes()
'''