import { Injectable } from '@angular/core';
import { environment } from '../enviroments/enviroment';
import { Periodos } from '../Common/periodos';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PeriodosService {

  private baseUrl=environment.MyAppApiUrl;
  private scheduleURL=this.baseUrl+'/schedulee/periodos_edificio/'

  constructor(private httpClient: HttpClient) { }

  getPeriodosEdificio(id:number): Observable<Periodos[]> {
    this.scheduleURL+=id;
    return this.httpClient.get<Periodos[]>(this.scheduleURL);
  }
  
}
