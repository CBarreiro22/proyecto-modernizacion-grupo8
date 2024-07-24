import { NgModule } from '@angular/core';
import {CommonModule, NgOptimizedImage} from '@angular/common';
import { AutomovilComponent } from './automovil.component';
import {RegistrarAutomovilComponent} from "./registrar-automovil/registrar-automovil.component";
import {ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";



@NgModule({
  declarations: [
    AutomovilComponent,
    RegistrarAutomovilComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    NgOptimizedImage,
    HttpClientModule
  ]
})
export class AutomovilModule { }
