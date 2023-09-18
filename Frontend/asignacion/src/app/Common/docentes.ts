import { Periodos } from "./periodos";

export class Docentes {
    id: number=0;
    nombre: string;
    apellido: string;
    horario_entrada: Date;
    horario_salida: Date;
    periodo_inicio: Periodos;
    periodo_fin: Periodos;
    
}
