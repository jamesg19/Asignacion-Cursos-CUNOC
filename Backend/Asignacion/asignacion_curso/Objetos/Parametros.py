class ParemetrosOBJ:


    def __init__(self,nombreHorario, semestre, ciclo, cantMinima,edificioId,
                 prioridadPorSemestreAscendente, prioridadPorSemestreDescendente,
                 prioridadPorDemanda, prioridadPorSemestreActual, elegirSalonExclusivo,
                 docentesenHorarioLaboral,capacidadSalon ):
        self.nombreHorario = nombreHorario
        self.semestre=semestre
        self.ciclo = ciclo
        self.cantMinima = cantMinima
        self.edificioId = edificioId


        self.prioridadPorSemestreAscendente = prioridadPorSemestreAscendente
        self.prioridadPorSemestreDescendente = prioridadPorSemestreDescendente
        self.prioridadPorDemanda = prioridadPorDemanda
        self.prioridadPorSemestreActual = prioridadPorSemestreActual
        self.elegirSalonExclusivo = elegirSalonExclusivo
        self.docentesenHorarioLaboral = docentesenHorarioLaboral
        self.capacidadSalon = capacidadSalon
