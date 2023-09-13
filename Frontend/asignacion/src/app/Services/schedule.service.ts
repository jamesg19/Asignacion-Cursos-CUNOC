import { Injectable } from '@angular/core';
import { environment } from '../enviroments/enviroment';
import { HorariosCursos } from '../Common/horarios-cursos';
import { Observable, map } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ScheduleService {
  private baseUrl=environment.MyAppApiUrl;
  private scheduleURL=this.baseUrl+'/schedulee/'

  constructor(private httpClient: HttpClient) { }

  getHorariosCursos(id:number): Observable<HorariosCursos[]> {
    this.scheduleURL+=id
    return this.httpClient.get<HorariosCursos[]>(this.scheduleURL);
  }
}




interface GetResponseHorariosCursos {
  
    horarios: HorariosCursos[];
  
}
