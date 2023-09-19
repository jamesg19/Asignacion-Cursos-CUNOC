import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, Validators } from '@angular/forms';
import { Horarios } from 'src/app/Common/horarios';
import { ParametrosService } from 'src/app/Services/parametros.service';
import { FormValidators } from 'src/app/Validators/form-validators';
import { Location } from '@angular/common';

@Component({
  selector: 'app-parametros',
  templateUrl: './parametros.component.html',
  styleUrls: ['./parametros.component.css']
})
export class ParametrosComponent {

  flag:number=0;
  parametrosForm: FormGroup;
  private horario:Horarios=new Horarios();
  urlActual:string = ""
  idHorarioGenerado:number=0;

  constructor(private formBuilder: FormBuilder,
    private parametrosService: ParametrosService,
    private location: Location){
    this.createForm();

  }
  
  createForm(){
    console.log("crear el form")
    this.parametrosForm = this.formBuilder.group({
        parametro: this.formBuilder.group({

            nombre:  new FormControl('', 
                                  [Validators.required, 
                                  Validators.minLength(2), 
                                  FormValidators.notOnlyWhitespace]),
            semestre:  [1],
            ciclo:  [2023],
            cantidad_minima:  [5],
            edificio_id:  [1],
            prioridad:  [1]   ,      
            elegir_salon_exclusivo:  [1],                    
            docente_horariolaboral:  [1]                      





      })
    });

    
  }

  onSubmit(){
    this.urlActual = this.location.path();
    this.flag=0;
    //alert(this.parametrosForm.get('parametro.nombre').value)
    let nombre:string=this.parametrosForm.get('parametro.nombre').value
    let semestre:number=+this.parametrosForm.get('parametro.semestre').value
    let ciclo:number=+this.parametrosForm.get('parametro.ciclo').value
    let cantidad_minima:number=+this.parametrosForm.get('parametro.cantidad_minima').value
    let edificio_id:number=+this.parametrosForm.get('parametro.edificio_id').value
    let prioridad:number=+this.parametrosForm.get('parametro.prioridad').value
    let elegir_salon_exclusivo:number=+this.parametrosForm.get('parametro.elegir_salon_exclusivo').value
    let docente_horariolaboral:number=+this.parametrosForm.get('parametro.docente_horariolaboral').value

    //Asignacion
    this.horario.nombre=nombre;
    this.horario.semestre=semestre;
    this.horario.ciclo=ciclo;
    this.horario.cantidad_minima=cantidad_minima;
    this.horario.edificio_id=edificio_id;
    this.validatePrioridad(+prioridad)

    if (elegir_salon_exclusivo==1){
      this.horario.elegir_salon_exclusivo=true;
    }else{
      this.horario.elegir_salon_exclusivo=false;
    }

    if (docente_horariolaboral==1){
      this.horario.docente_horariolaboral=true;
    }else{
      this.horario.docente_horariolaboral=false;
    }
   

    //impimir todas las variables declaradas
    console.log("nombre: "+nombre)
    console.log("semestre: "+semestre)
    console.log("ciclo: "+ciclo)  
    console.log("cantidad_minima: "+cantidad_minima)
    console.log("edificio_id: "+edificio_id)  
    console.log("prioridad: "+prioridad)  
    console.log("elegir_salon_exclusivo: "+elegir_salon_exclusivo)
    console.log("docente_horariolaboral: "+docente_horariolaboral)  



    this.simular();


    /*if (this.parametrosForm.invalid) {
      this.parametrosForm.markAllAsTouched();
      return;
    }*/
    
  }
  private simular(){
    this.parametrosService.simularConParametros(this.horario).subscribe(
      data=>{
        this.flag=1;
        this.idHorarioGenerado=data['id'];  
        console.log("Simulacion exitosa")
      }, 
      error=>{
        this.flag=2;
        console.log("Simulacion fallida")
      }
    )
  }
  private validatePrioridad(prioridad:number){

    switch(prioridad){
      case 1:
        this.horario.prioridad_semestre_ascendente=false;
        this.horario.prioridad_semestre_descendente=false;
        this.horario.prioridad_demanda=false;
        this.horario.prioridad_semestre_actual=true;
        break;
      case 2: 
        this.horario.prioridad_semestre_ascendente=true;
        this.horario.prioridad_semestre_descendente=false;
        this.horario.prioridad_demanda=false;
        this.horario.prioridad_semestre_actual=false;
        break;
      case 3: 
        this.horario.prioridad_semestre_ascendente=false;
        this.horario.prioridad_semestre_descendente=true;
        this.horario.prioridad_demanda=false;
        this.horario.prioridad_semestre_actual=false;
        break;
      case 4: 
        this.horario.prioridad_semestre_ascendente=false;
        this.horario.prioridad_semestre_descendente=false;
        this.horario.prioridad_demanda=true;
        this.horario.prioridad_semestre_actual=false;
        break;
    }
  }

}
