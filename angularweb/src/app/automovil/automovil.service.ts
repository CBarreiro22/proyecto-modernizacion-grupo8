import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable, of} from "rxjs";
import {environment} from "../../environments/environment.prod";

@Injectable({
  providedIn: 'root'
})
export class AutomovilService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  registerCar(dataParameter: any): Observable<any> {
    return this.http.post(`${this.apiUrl}`+'/v1/car', dataParameter);
  }
  listCar(): Observable<any> {
    return this.http.get(`${this.apiUrl}`+'/v1/car');
  }
}
