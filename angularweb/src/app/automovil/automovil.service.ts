import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AutomovilService {

  constructor(private http: HttpClient) { }

  registerCar(dataParameter: FormData): Observable<any> {
    return this.http.post('http://localhost:3000/api/automovil', dataParameter);
  }
}
