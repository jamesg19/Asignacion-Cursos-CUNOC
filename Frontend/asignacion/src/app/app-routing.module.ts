import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TablaHorarioComponent } from './Components/tabla-horario/tabla-horario.component';
import { ProcessComponent } from './Components/process/process.component';
import { ParametrosComponent } from './Components/parametros/parametros.component';
import { ListScheduleComponent } from './Components/list-schedule/list-schedule.component';

const routes: Routes = [
  {path:'schedule/:idHorario',component: TablaHorarioComponent },
  {path:'parametros',component: ParametrosComponent },
  {path:'list_schedule',component: ListScheduleComponent },
  {path:'',component: ProcessComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
