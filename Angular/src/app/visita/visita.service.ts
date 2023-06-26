import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VisitaService {

  constructor(private http: HttpClient) { }

  public getVisitas(personData: any): Observable<any> {

    let url: string = "http://34.16.150.201:4201/visitas";
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    });
    return this.http.get(url, { headers: headers });
  }

  public getVisita(id: any): Observable<any> {

    let url: string = "http://34.16.150.201:4201/detallevisita/1"
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    });
    return this.http.get(url, { headers: headers });
  }
}
