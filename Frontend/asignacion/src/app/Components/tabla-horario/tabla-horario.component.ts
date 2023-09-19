import { Component, ElementRef, ViewChild } from '@angular/core';
import { Cursos } from 'src/app/Common/cursos';
import { HorariosCursos } from 'src/app/Common/horarios-cursos';
import { Periodos } from 'src/app/Common/periodos';
import { Salones } from 'src/app/Common/salones';
import { PeriodosService } from 'src/app/Services/periodos.service';
import { SalonesService } from 'src/app/Services/salones.service';
import { ScheduleService } from 'src/app/Services/schedule.service';
import { ActivatedRoute } from '@angular/router';
import { Horarios } from 'src/app/Common/horarios';
import html2canvas from 'html2canvas';
import jspdf from 'jspdf';
import { Docentes } from 'src/app/Common/docentes';
import { ParametrosService } from 'src/app/Services/parametros.service';


@Component({
  selector: 'app-tabla-horario',
  templateUrl: './tabla-horario.component.html',
  styleUrls: ['./tabla-horario.component.css']
})
export class TablaHorarioComponent {
  @ViewChild('tablaHTML') tablaHTML: ElementRef;

  horario:Horarios;
  horariosCursos:HorariosCursos[]=[]
  salonesUnicos:Salones[]=[]
  private listHorariosLibres:HorariosCursos[]=[];
  periodosUnicos:Periodos[]=[]
  idHorario: number 

  eficaciaPromedioSalones:number=0;
  eficaciaPromedioPeriodos:number=0;
  eficaciaPromedioCursosConDocentes:number=0;
  eficaciaDocenteHorarioLaboral:number=0;
  eficaciaTotal:number=0;

  


  constructor(private scheduleService: ScheduleService, 
    private periodosService:PeriodosService,
    private salonesService:SalonesService,
    private parametrosService:ParametrosService,
    private route: ActivatedRoute) { }


  ngOnInit() {
      this.idHorario= +this.route.snapshot.paramMap.get('idHorario');
      this.listPeriodos();
      this.listSalones();
      this.listParametros();
      this.listSchedule();

      

    
  }
  private listParametros(){
    console.log("listParametros called");
    this.parametrosService.getParametrosHorario(this.idHorario)
      .subscribe(data => {
        console.log(data);   
        this.horario=data;
      });

  }
  getClassForNombre(idCarrera: number): string {
    if (idCarrera === 5) {
      return 'punto_carrera_sistemas';
    } 
    else if (idCarrera === 2)  {
      return 'punto_carrera_industrial';
    } 
    else{
      return ''
    }
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

  private eficacia(){
    let tempSalon:number=0;
    let contadorSalon:number=0;
    let tempPeriodo:number=0;
    let contadorPeriodo:number=0;
    //salones
    for (let i =0;i<this.salonesUnicos.length;i++){
  
      let salonesOcupados=this.horariosCursos.filter(horario => horario.salon.id === this.salonesUnicos[i].id && horario.id !== 0 )
      
      console.log(this.salonesUnicos[i].nombre);

      this.salonesUnicos[i].eficacia= (  (salonesOcupados.length)/(this.periodosUnicos.length)  )*100
      this.salonesUnicos[i].eficacia.toFixed(2)
      let temp=this.salonesUnicos[i].eficacia
      if (temp>0){
        tempSalon=tempSalon+temp;
        contadorSalon+=1;
      }
      //this.salonesUnicos[i].eficacia.toFixed(2)
      tempSalon.toFixed(2)
    }
    this.eficaciaPromedioSalones= (tempSalon/contadorSalon)
    this.eficaciaPromedioSalones.toFixed(2) 

    //periodos
    for (let i =0;i<this.periodosUnicos.length;i++){
      const periodosOcupados=this.horariosCursos.filter(horario => horario.periodo_inicio.id === this.periodosUnicos[i].id && horario.id !== 0)

      this.periodosUnicos[i].eficacia= (  (periodosOcupados.length)/(this.salonesUnicos.length)  )*100
      this.periodosUnicos[i].eficacia.toFixed(2)
      if(this.periodosUnicos[i].eficacia>0 ){
        tempPeriodo+= this.periodosUnicos[i].eficacia
        contadorPeriodo+=1;
      }
     
      
    }
    this.eficaciaPromedioPeriodos=tempPeriodo/contadorPeriodo
    this.eficaciaPromedioPeriodos.toFixed(2)
    this.eficaciaTotal=(this.eficaciaPromedioSalones+this.eficaciaPromedioPeriodos+this.eficaciaPromedioCursosConDocentes+this.eficaciaDocenteHorarioLaboral)/4
    console.log("sale")
  }

  private listSchedule() {
    console.log("listSchedule called")
    
    this.scheduleService.getHorariosCursos(this.idHorario)
      .subscribe(data => {
        this.horariosCursos=data;
        //console.log("HorariosCursos: "+this.horariosCursos);
        this.procesarDatos();
        this.eficacia();
        this.ajustarTabla();
      });

  }


  private procesarDatos(){

    let tempConDocente:number=0;
    let tempHorrioLaboral:number=0;

    this.horariosCursos.forEach(item => {
      if(item.docente !== null ){
        //if(item.docente?.id !== 0){
          tempConDocente+=1;
        //}
        
      }
      if(item.disponible_en_horario_laboral == true){
        tempHorrioLaboral+=1;
      }
      console.log()
    });
    this.eficaciaPromedioCursosConDocentes=(tempConDocente/this.horariosCursos.length)*100;
    this.eficaciaPromedioCursosConDocentes.toFixed(2);

    this.eficaciaDocenteHorarioLaboral=(tempHorrioLaboral/this.horariosCursos.length)*100;
    this.eficaciaDocenteHorarioLaboral.toFixed(2);



    
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
            //console.log("   Hay libre en: \nSalon: "+this.salonesUnicos[i].id+" Periodo: "+this.periodosUnicos[j].id)
            this.crearLibre(i,j);
          }
        
      }
      
    }


   



  }

  private crearLibre(i,j){
    
      //console.log("Entra en periodo libre");

      let periodo_inicio:Periodos=new Periodos();
      periodo_inicio.id=this.periodosUnicos[j].id;

      let salon:Salones=new Salones();
      salon.id=this.salonesUnicos[i].id;
      //console.log("Salon: "+salon.id+" Periodo: "+periodo_inicio.id+"")

      let curso:Cursos=new Cursos();
      curso.id_curso=0;
      curso.nombre_curso="";
      curso.duracion_periodo=1;

      let docente:Docentes=new Docentes();
      docente.id=0;
      
      //crear objeto horarioCursos
      let horario:HorariosCursos=new HorariosCursos();

      horario.id=0;
      horario.periodo_inicio=periodo_inicio;
      horario.periodo_fin=periodo_inicio;
      horario.salon=salon;
      horario.curso=curso;
      horario.docente=docente;

      this.listHorariosLibres.push(horario);
      this.horariosCursos.push(horario);
  }




  descargarPDF() {
    const content: HTMLElement = this.tablaHTML.nativeElement;

    html2canvas(content).then(canvas => {
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jspdf('l', 'mm', 'legal');
      
      const imgProps = pdf.getImageProperties(imgData);
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;

      pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
      pdf.save('tabla.pdf');
    });
  }



  private ajustarTabla(){
    

  }

  private processResult() {
    return data => {
      this.horariosCursos=data;
      
    };
  }
  

}
