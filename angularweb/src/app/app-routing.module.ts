import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AutomovilComponent} from "./automovil/automovil.component";

const routes: Routes = [
  {'path': '', 'component': AutomovilComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
