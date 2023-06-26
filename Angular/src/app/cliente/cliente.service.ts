import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {

  constructor(private http: HttpClient) { }

  public getClients(personData: any): Observable<any> {

    let url: string = "http://34.16.150.201:4201/cliente";
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    });
    return this.http.get(url, { headers: headers });
  }

  public nuevoCliente(datoscliente: any) {

    let url: string = "http://34.16.150.201:4201/cliente";
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    });

    console.log("invocando servicio web ....");
    return this.http.post(url,
      JSON.stringify(datoscliente),
      { headers: headers });
  }

}

