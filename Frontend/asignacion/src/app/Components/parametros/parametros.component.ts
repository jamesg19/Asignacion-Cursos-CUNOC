import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, Validators } from '@angular/forms';
import { FormValidators } from 'src/app/Validators/form-validators';

@Component({
  selector: 'app-parametros',
  templateUrl: './parametros.component.html',
  styleUrls: ['./parametros.component.css']
})
export class ParametrosComponent {


  parametrosForm: FormGroup;

  constructor(private formBuilder: FormBuilder){
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
            semestre:  new FormControl('', 
                                  [Validators.required, 
                                  Validators.minLength(2), 
                                  FormValidators.notOnlyWhitespace]),
            ciclo:  new FormControl('', 
                                  [Validators.required, 
                                  Validators.minLength(2), 
                                  FormValidators.notOnlyWhitespace]),
            cantidad_minima:  new FormControl('', 
                                  [Validators.required, 
                                  Validators.minLength(2), 
                                  FormValidators.notOnlyWhitespace]),
            edificio_id:  new FormControl('', 
                                  [Validators.required, 
                                  Validators.minLength(2), 
                                  FormValidators.notOnlyWhitespace]),
            prioridad:  new FormControl('', 
                                  [Validators.required, 
                                  Validators.minLength(2), 
                                  FormValidators.notOnlyWhitespace]), 
                prioridad_semestre_ascendente:  new FormControl('', 
                                      [Validators.required, 
                                      Validators.minLength(2), 
                                      FormValidators.notOnlyWhitespace]),
                prioridad_semestre_descendente:  new FormControl('', 
                                      [Validators.required, 
                                      Validators.minLength(2), 
                                      FormValidators.notOnlyWhitespace]),  
                prioridad_demanda:  new FormControl('', 
                                      [Validators.required, 
                                      Validators.minLength(2), 
                                      FormValidators.notOnlyWhitespace]),                      
                prioridad_semestre_actual:  new FormControl('', 
                                      [Validators.required, 
                                      Validators.minLength(2), 
                                      FormValidators.notOnlyWhitespace]),              
            elegir_salon_exclusivo:  new FormControl('', 
                                  [Validators.required, 
                                  Validators.minLength(2), 
                                  FormValidators.notOnlyWhitespace]),                      
            docente_horariolaboral:  new FormControl('', 
                                  [Validators.required, 
                                  Validators.minLength(2), 
                                  FormValidators.notOnlyWhitespace]),                       





      })
    });

    
  }

  onSubmit(){

    
    alert(this.parametrosForm.get('parametro.nombre'))
    console.log("ENtraaaaa")

    /*if (this.parametrosForm.invalid) {
      this.parametrosForm.markAllAsTouched();
      return;
    }*/
    return
  }

}
