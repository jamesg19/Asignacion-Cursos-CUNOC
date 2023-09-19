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
    this.parametrosService.deleteHorario(id).subscribe(
      data=>{
        for(let item of this.horarios){
          if(item.id==id){
            this.horarios.splice(this.horarios.indexOf(item),1);
          }

        }
        

      }, 
      error=>{
       
      }
    )
  }

  getListSchedule(){
    this.parametrosService.getSchedules().subscribe(
      data=>{
        
        this.horarios=data;
        console.log(data)

      }, 
      error=>{
        alert("Error al obtener los horarios")
      }
    )




  }

}
