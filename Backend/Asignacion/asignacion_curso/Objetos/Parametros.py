class ParemetrosOBJ:

    def __init__(self, nombre, semestre, ciclo, cantidad_minima, edificio_id,
                 prioridad_semestre_ascendente, prioridad_semestre_descendente,
                 prioridad_demanda, prioridad_semestre_actual, elegir_salon_exclusivo,
                 docente_horariolaboral, capacidadSalon):
        self.nombre = nombre
        self.semestre = semestre
        self.ciclo = ciclo
        self.cantidad_minima = cantidad_minima
        self.edificio_id = edificio_id

        self.prioridad_semestre_ascendente = prioridad_semestre_ascendente
        self.prioridad_semestre_descendente = prioridad_semestre_descendente
        self.prioridad_demanda = prioridad_demanda
        self.prioridad_semestre_actual = prioridad_semestre_actual
        self.elegir_salon_exclusivo = elegir_salon_exclusivo
        self.docente_horariolaboral = docente_horariolaboral
        self.capacidadSalon = capacidadSalon
