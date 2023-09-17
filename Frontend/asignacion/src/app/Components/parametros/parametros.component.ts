import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, Validators } from '@angular/forms';
import { FormValidators } from 'src/app/Validators/form-validators';

@Component({
  selector: 'app-parametros',
  templateUrl: './parametros.component.html',
  styleUrls: ['./parametros.component.css']
})
export class ParametrosComponent implements OnInit {


  parametrosForm: FormGroup;

  constructor(private formBuilder: FormBuilder){
   
  }
  ngOnInit(): void {
    this.createForm();
    
  }
  createForm(){
    console.log("crear el form")
    this.parametrosForm = this.formBuilder.group({
      parametro: this.formBuilder.group({

        nombreHorario:  new FormControl('', 
                              [Validators.required, 
                               Validators.minLength(2), 
                               FormValidators.notOnlyWhitespace])
        
      })
    });
  }

  onSubmit(){

    
    alert(this.parametrosForm.get('parametro.nombreHorario'))
    console.log("ENtraaaaa")

    /*if (this.parametrosForm.invalid) {
      this.parametrosForm.markAllAsTouched();
      return;
    }*/
    return
  }

}
