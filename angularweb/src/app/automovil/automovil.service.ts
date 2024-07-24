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
}
