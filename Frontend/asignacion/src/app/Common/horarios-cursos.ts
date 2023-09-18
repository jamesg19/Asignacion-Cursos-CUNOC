import { Carrera } from "./carrera";
import { Cursos } from "./cursos";
import { Docentes } from "./docentes";
import { Horarios } from "./horarios";
import { Periodos } from "./periodos";
import { Salones } from "./salones";

export class HorariosCursos {
    id: number;
    horario: Horarios;
    curso: Cursos;
    docente: Docentes;
    salon: Salones;
    seccion: string;
    carrera:Carrera;
    dias_semana: string;
    periodo_inicio: Periodos;
    periodo_fin: Periodos;
    asignados: number;
    capacidad: number;
    disponible_en_horario_laboral:boolean;
    
}
