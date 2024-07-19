import {Component, inject, TemplateRef} from '@angular/core';
import {NgOptimizedImage} from "@angular/common";
import {NgbModal} from "@ng-bootstrap/ng-bootstrap";
import {RegistrarAutomovilComponent} from "../automovil/registrar-automovil/registrar-automovil.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    NgOptimizedImage,
    RegistrarAutomovilComponent
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  private modalService = inject(NgbModal);

  openVerticallyCentered(content: TemplateRef<any>) {
    this.modalService.open(content, { centered: true });
  }

}
