import {Component, EventEmitter, Input, Output} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {AutomovilService} from "../automovil.service";

@Component({
  selector: 'app-registrar-automovil',
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
    if (this.myForm.valid) {
      this.automovilService.registerCar(this.myForm.value).subscribe({
        next: () => {
          this.registroExitoso.emit(true);
          this.modal.close();
        },
        error: (err) => {
          console.error('Error registrando automóvil', err);
        }
      });
    }
  }
}
