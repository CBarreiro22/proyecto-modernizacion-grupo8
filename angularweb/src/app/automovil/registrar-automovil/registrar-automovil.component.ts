import {Component, EventEmitter, Input, Output} from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {NgIf} from "@angular/common";
import {AutomovilService} from "../automovil.service";

@Component({
  selector: 'app-registrar-automovil',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    NgIf
  ],
  templateUrl: './registrar-automovil.component.html',
  styleUrl: './registrar-automovil.component.css'
})
export class RegistrarAutomovilComponent {
  @Input() modal: any;
  myForm: FormGroup;
  @Output() registroExitoso = new EventEmitter<boolean>();

  constructor(private fb: FormBuilder, private automovilService: AutomovilService ) {
    this.myForm = this.fb.group({
      marca: ['', [Validators.required, Validators.minLength(6), Validators.maxLength(10), Validators.pattern('[a-zA-Z0-9]+')]],
      placa: ['', [Validators.required, Validators.minLength(3), Validators.maxLength(255), Validators.pattern('[a-zA-Z0-9]+')]],
      modelo: ['', [Validators.required, Validators.min(1886)]],
      kilometraje: ['', [Validators.required, Validators.min(0), Validators.max(999999999)]],
      color: ['', [Validators.required, Validators.minLength(3), Validators.maxLength(255), Validators.pattern('[a-zA-Z0-9]+')]],
      cilindraje: ['', [Validators.required, Validators.min(0), Validators.max(999999999)]],
      tipoDeCombustible: ['', [Validators.required, Validators.minLength(3), Validators.maxLength(255), Validators.pattern('[a-zA-Z0-9]+')]],
    });
  }


  onSubmit() {
    const formData = new FormData();
    formData.append('marca', this.myForm.value.marca);
    formData.append('placa', this.myForm.value.placa);
    formData.append('modelo', this.myForm.value.modelo);
    formData.append('kilometraje', this.myForm.value.kilometraje);
    formData.append('color', this.myForm.value.color);
    formData.append('cilindraje', this.myForm.value.cilindraje);
    formData.append('tipoDeCombustible', this.myForm.value.tipoDeCombustible);
    this.automovilService.registerCar(formData).subscribe(()=>{
      this.registroExitoso.emit(true);
      this.modal.close()
    })
  }
}
