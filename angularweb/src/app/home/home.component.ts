import {Component, inject, TemplateRef} from '@angular/core';
import {NgIf, NgOptimizedImage} from "@angular/common";
import {NgbModal} from "@ng-bootstrap/ng-bootstrap";
import {RegistrarAutomovilComponent} from "../automovil/registrar-automovil/registrar-automovil.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    NgOptimizedImage,
    RegistrarAutomovilComponent,
    NgIf
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  private modalService = inject(NgbModal);
  registroExitoso: boolean = false;

  openVerticallyCentered(content: TemplateRef<any>) {
    this.modalService.open(content, { centered: true });
  }

  onRegistroExitoso(success: boolean) {
    this.registroExitoso = success;

    if (success) {
      setTimeout(() => {
        this.registroExitoso = false;
      }, 2000);
    }
  }
}
