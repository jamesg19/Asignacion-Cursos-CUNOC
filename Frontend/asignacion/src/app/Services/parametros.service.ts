import { Injectable } from '@angular/core';
import { environment } from '../enviroments/enviroment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Horarios } from '../Common/horarios';
import { Location } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class ParametrosService {

  private baseUrl=environment.MyAppApiUrl;
  


  constructor(private httpClient: HttpClient) { }

  getParametrosHorario(id:number): Observable<Horarios> {
    let scheduleURL=this.baseUrl
    scheduleURL+='/schedulee/parametros/'+id;
    return this.httpClient.get<Horarios>(scheduleURL);
  }

  getSchedules(): Observable<Horarios[]> {
    let scheduleURL=this.baseUrl
    scheduleURL+='/schedulee/list_schedulee/';
    return this.httpClient.get<Horarios[]>(scheduleURL);
  }
  deleteHorario(id:number): Observable<any> {
    let scheduleURL=this.baseUrl
    scheduleURL+='/schedulee/delete_horario/'+id;
    return this.httpClient.get<any>(scheduleURL);
  }

  simularConParametros(horarios:Horarios){
    let scheduleURL=this.baseUrl
    let url=scheduleURL+'/simular/'
    return this.httpClient.post<Horarios>(url,horarios);
  } 
}
