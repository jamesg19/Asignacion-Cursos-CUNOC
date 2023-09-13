import { Injectable } from '@angular/core';
import { environment } from '../enviroments/enviroment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Salones } from '../Common/salones';

@Injectable({
  providedIn: 'root'
})
export class SalonesService {

  private baseUrl=environment.MyAppApiUrl;
  private scheduleURL=this.baseUrl+'/schedulee/salones_edificio/'

  constructor(private httpClient: HttpClient) { }

  getSalonesEdificio(id:number): Observable<Salones[]> {
    this.scheduleURL+=id;
    return this.httpClient.get<Salones[]>(this.scheduleURL);
  }
}
