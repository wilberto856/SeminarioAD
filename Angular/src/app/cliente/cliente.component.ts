import { Component, OnInit } from '@angular/core';
import { ClienteService } from './cliente.service';

@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.css']
})
export class ClienteComponent implements OnInit {

  clientes: any;

  constructor(private clienteService: ClienteService) { }

  ngOnInit(): void {
    this.getClientes();
  }

  getClientes(): void {

    this.clienteService
      .getClients(null)
      .subscribe(
        data => {
          this.clientes = data
          console.log(data);
        },
        error => {
          console.log(error);
        }
      )
  }
}
