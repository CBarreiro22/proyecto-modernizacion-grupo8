import {Component, inject, OnInit, TemplateRef} from '@angular/core';
import {NgbModal} from "@ng-bootstrap/ng-bootstrap";
import {AutomovilService} from "./automovil.service";


@Component({
  selector: 'app-automovil',
  templateUrl: './automovil.component.html',
  styleUrl: './automovil.component.css'
})
export class AutomovilComponent implements OnInit{
  private modalService = inject(NgbModal);
  registroExitoso: boolean = false;
  selectedOption: string = 'Automovil';

  listaOpcionesC: any[] = [];
  listaOpcionesM: any[] = [];
  constructor(private automovilService: AutomovilService) {}

  ngOnInit() {
    this.automovilService.listCar().subscribe(resp => {
      if (Array.isArray(resp)) {
        this.listaOpcionesC = resp;
      } else {
        this.listaOpcionesC = [];
      }

      if (this.listaOpcionesC.length > 0) {
        this.ordenarListaPorPlacaDescendente();
      }
    });
  }

  openVerticallyCentered(content: TemplateRef<any>) {
    this.modalService.open(content, { centered: true });
  }
  ordenarListaPorPlacaDescendente() {
    this.listaOpcionesC.sort((a, b) => b.placa.localeCompare(a.placa));
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
