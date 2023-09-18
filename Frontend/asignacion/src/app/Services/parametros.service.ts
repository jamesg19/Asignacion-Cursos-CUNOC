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
  private scheduleURL=this.baseUrl


  constructor(private httpClient: HttpClient) { }

  getParametrosHorario(id:number): Observable<Horarios> {
    this.scheduleURL+='/schedulee/parametros/'+id;
    return this.httpClient.get<Horarios>(this.scheduleURL);
  }

  simularConParametros(horarios:Horarios){
    
    const url=this.scheduleURL+'/simular/'
    return this.httpClient.post<Horarios>(url,horarios);
  } 
}
