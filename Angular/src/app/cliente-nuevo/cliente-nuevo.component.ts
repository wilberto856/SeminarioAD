import { Component, OnInit } from '@angular/core';
import { ClienteService } from '../cliente/cliente.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-cliente-nuevo',
  templateUrl: './cliente-nuevo.component.html',
  styleUrls: ['./cliente-nuevo.component.css']
})
export class ClienteNuevoComponent implements OnInit {
  
  constructor(private clienteService: ClienteService) { }

  ngOnInit(): void {
    
  }
  
  onClickSubmit(result: NgForm) {

    this.clienteService
            .nuevoCliente(result)
            .subscribe(
                resultFromService => {
                    console.log("Resultado de server:" + JSON.stringify(resultFromService))
                });
    result.resetForm();
    
  }
}
