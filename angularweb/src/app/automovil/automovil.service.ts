import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable, of} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AutomovilService {

  constructor(private http: HttpClient) { }

  registerCar(dataParameter: any): Observable<any> {
    // Simula una respuesta exitosa
    const mockResponse = {
      success: true,
      message: 'Car registered successfully'
    };

    // Devuelve la respuesta simulada como un observable
    return of(mockResponse);

    // Si en algún momento necesitas realizar la solicitud real, puedes comentar la línea anterior y descomentar la siguiente:
    // return this.http.post('https://yriu3qxzo4.execute-api.us-east-1.amazonaws.com/v1/car', dataParameter);
  }
  listCar(): Observable<any> {
    // Simula una respuesta exitosa
    const mockResponse = {
      success: true,
      message: [
        {
          marca: 'Toyota',
          placa: 'ABC123',
          modelo: 2021,
          kilometraje: 1000,
          color: 'Rojo',
          cilindraje: 2000,
          tipoDeCombustible: 'Gasolina'
        },
        {
          marca: 'Chevrolet',
          placa: 'DEF456',
          modelo: 2020,
          kilometraje: 2000,
          color: 'Azul',
          cilindraje: 1500,
          tipoDeCombustible: 'Gasolina'
        },
        {
          marca: 'Mazda',
          placa: 'GHI789',
          modelo: 2021,
          kilometraje: 500,
          color: 'Blanco',
          cilindraje: 1800,
          tipoDeCombustible: 'Gasolina'
        },
        {
          marca: 'Ford',
          placa: 'JKL012',
          modelo: 2022,
          kilometraje: 0,
        }
      ]
    };

    // Devuelve la respuesta simulada como un observable
    return of(mockResponse);

    // Si en algún momento necesitas realizar la solicitud real, puedes comentar la línea anterior y descomentar la siguiente:
    // return this.http.get('https://yriu3qxzo4.execute-api.us-east-1.amazonaws.com/v1/car');
  }
}
