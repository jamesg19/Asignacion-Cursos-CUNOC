import { Injectable } from '@angular/core';
import { environment } from '../enviroments/enviroment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Horarios } from '../Common/horarios';

@Injectable({
  providedIn: 'root'
})
export class ParametrosService {

  private baseUrl=environment.MyAppApiUrl;
  private scheduleURL=this.baseUrl+'/schedulee/parametros/'

  constructor(private httpClient: HttpClient) { }

  getParametrosHorario(id:number): Observable<Horarios> {
    this.scheduleURL+=id;
    return this.httpClient.get<Horarios>(this.scheduleURL);
  }
}
