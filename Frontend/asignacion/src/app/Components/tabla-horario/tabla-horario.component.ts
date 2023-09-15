import { Component } from '@angular/core';
import { Cursos } from 'src/app/Common/cursos';
import { HorariosCursos } from 'src/app/Common/horarios-cursos';
import { Periodos } from 'src/app/Common/periodos';
import { Salones } from 'src/app/Common/salones';
import { PeriodosService } from 'src/app/Services/periodos.service';
import { SalonesService } from 'src/app/Services/salones.service';
import { ScheduleService } from 'src/app/Services/schedule.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-tabla-horario',
  templateUrl: './tabla-horario.component.html',
  styleUrls: ['./tabla-horario.component.css']
})
export class TablaHorarioComponent {



  horariosCursos:HorariosCursos[]=[]
  salonesUnicos:Salones[]=[]
  private listHorariosLibres:HorariosCursos[]=[];
  periodosUnicos:Periodos[]=[]


  constructor(private scheduleService: ScheduleService, 
    private periodosService:PeriodosService,
    private salonesService:SalonesService,
    private route: ActivatedRoute) { }


  ngOnInit() {
      this.listPeriodos();
      this.listSalones();
      this.listSchedule();

    
  }

  private listPeriodos() {
    console.log("listPeriodos called");
    this.periodosService.getPeriodosEdificio(1)
    .subscribe(data =>{
      this.periodosUnicos=data;
    });
  }
  private listSalones() {
    console.log("listSalones called");

    this.salonesService.getSalonesEdificio(1).subscribe(data =>{
      this.salonesUnicos=data;
    });

  }

  private listSchedule() {
    console.log("listSchedule called")
    let idHorario= +this.route.snapshot.paramMap.get('idHorario');
    this.scheduleService.getHorariosCursos(10)
      .subscribe(data => {
        this.horariosCursos=data;
        this.procesarDatos();
      });

  }


  procesarDatos(){
    
    //Eje X
    for (let i = 0; i < this.salonesUnicos.length; i++) {
      
      // Eje Y
      for( let j=0; j < this.periodosUnicos.length; j++){
          let tempI=0;
          let tempJ=0;
          let flag=false;

          let periodoTmp=this.horariosCursos.find(horario => horario.periodo_inicio.id === this.periodosUnicos[j].id && horario.salon.id === this.salonesUnicos[i].id )
          if(periodoTmp){
            //console.log("   Hay clase en: \nSalon: "+this.salonesUnicos[i].id+" Periodo: "+this.periodosUnicos[j].id)
          }else{
            //imprimir salon libre en i y peiodo libre en j
            console.log("   Hay libre en: \nSalon: "+this.salonesUnicos[i].id+" Periodo: "+this.periodosUnicos[j].id)
            this.crearLibre(i,j);
          }
          /*
          let periodoTmp=this.horariosCursos.find(horario => horario.periodo_inicio.id === this.periodosUnicos[j].id )
          let salonTmp=this.horariosCursos.find(horario => horario.salon.id === this.salonesUnicos[i].id )

          if (!periodoTmp && salonTmp){

            console.log("   Hay libre en: \nSalon: "+this.salonesUnicos[i].id+" Periodo: "+this.periodosUnicos[j].id)
          }
          if (!salonTmp && periodoTmp){

            console.log("   Hay libre en: \nSalon: "+this.salonesUnicos[i].id+" Periodo: "+this.periodosUnicos[j].id)
          }*/

        
      }
      
    }


   



  }

  private crearLibre(i,j){
    
      console.log("Entra en periodo libre");

      let periodo_inicio:Periodos=new Periodos();
      periodo_inicio.id=this.periodosUnicos[j].id;

      let salon:Salones=new Salones();
      salon.id=this.salonesUnicos[i].id;

      let curso:Cursos=new Cursos();
      curso.id_curso=0;
      curso.nombre_curso="";
      curso.duracion_periodo=1;
      
      //crear objeto horarioCursos
      let horario:HorariosCursos=new HorariosCursos();

      horario.id=0;
      horario.periodo_inicio=periodo_inicio;
      horario.periodo_fin=periodo_inicio;
      horario.salon=salon;
      horario.curso=curso;

      this.listHorariosLibres.push(horario);
      this.horariosCursos.push(horario);
  }










  private processResult() {
    return data => {
      this.horariosCursos=data;
      
    };
  }

}
