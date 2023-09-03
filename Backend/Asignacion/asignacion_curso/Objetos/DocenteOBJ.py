class DocenteOBJ:
    def __init__(self, id, nombre, apellido, horario_entrada, horario_salida, titular):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.horario_entrada = horario_entrada
        self.horario_salida = horario_salida
        self.titular = titular

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'horario_entrada': self.horario_entrada,
            'horario_salida': self.horario_salida,
            'titular': self.titular
        }
