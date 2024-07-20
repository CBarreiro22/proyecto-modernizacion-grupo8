import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {AbstractControl, FormBuilder, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {NgIf} from "@angular/common";

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
export class RegistrarAutomovilComponent implements OnInit {
  @Input() modal: any;
  myForm: FormGroup;
  @Output() registroExitoso = new EventEmitter<boolean>();

  constructor(private fb: FormBuilder) {
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



  ngOnInit() {

  }


  onSubmit() {
    this.registroExitoso.emit(true);
    this.modal.close()
  }
}
