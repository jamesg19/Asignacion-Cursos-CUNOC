import { Component } from '@angular/core';
import { Horarios } from 'src/app/Common/horarios';
import { ParametrosService } from 'src/app/Services/parametros.service';
import { environment } from 'src/app/enviroments/enviroment';

@Component({
  selector: 'app-list-schedule',
  templateUrl: './list-schedule.component.html',
  styleUrls: ['./list-schedule.component.css']
})
export class ListScheduleComponent {
  horarios:Horarios[];
  private baseUrl=environment.MyAppApiUrl;
  constructor(private parametrosService: ParametrosService){
    this. getListSchedule();

  }
  verHorario(id:number){
    window.open("http://localhost:4200/schedule/"+id, '_blank');
  }

  eliminarHorario(id:number){
    //window.open(this.baseUrl+"/schedulee/"+id, '_blank');
  }

  getListSchedule(){
    this.parametrosService.getSchedules().subscribe(
      data=>{
        
        this.horarios=data;

      }, 
      error=>{
        alert("Error al obtener los horarios")
      }
    )




  }

}
