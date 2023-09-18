export class Horarios {
    id:number;
    nombre: string;
    semestre: number;
    ciclo: number;
    cantidad_minima: number;
    edificio_id: number;
    prioridad_semestre_ascendente: boolean;
    prioridad_semestre_descendente: boolean;
    prioridad_demanda: boolean;
    prioridad_semestre_actual: boolean;
    elegirSalonExclusivo: boolean;
    docente_horariolaboral: boolean;
    capacidadSalon: number;
}
