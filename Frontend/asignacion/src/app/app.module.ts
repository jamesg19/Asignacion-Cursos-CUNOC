import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Routes, RouterModule, Router } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TablaHorarioComponent } from './Components/tabla-horario/tabla-horario.component';
import { NavbarComponent } from './Components/navbar/navbar.component';
import { HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { ProcessComponent } from './Components/process/process.component';
import { ParametrosComponent } from './Components/parametros/parametros.component'
import { ReactiveFormsModule } from '@angular/forms';




@NgModule({
  declarations: [
    AppComponent,
    TablaHorarioComponent,
    NavbarComponent,
    ProcessComponent,
    ParametrosComponent
  ],
  imports: [

    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule   
  ],
  
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
