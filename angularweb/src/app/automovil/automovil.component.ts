import {Component, inject, TemplateRef} from '@angular/core';
import {NgbModal} from "@ng-bootstrap/ng-bootstrap";


@Component({
  selector: 'app-automovil',
  templateUrl: './automovil.component.html',
  styleUrl: './automovil.component.css'
})
export class AutomovilComponent {
  private modalService = inject(NgbModal);
  registroExitoso: boolean = false;
  selectedOption: string = 'Automovil';

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

  openVerticallyCentered2(content: TemplateRef<any>) {

  }
}
