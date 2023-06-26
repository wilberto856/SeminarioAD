import { Component, OnInit } from '@angular/core';
import { EstadoService } from './estado.service';

@Component({
  selector: 'app-estado',
  templateUrl: './estado.component.html',
  styleUrls: ['./estado.component.css']
})
export class EstadoComponent implements OnInit {

  estados: any;

  constructor(private estadoService: EstadoService) { }

  ngOnInit(): void {
    this.getEstados();
  }

  getEstados(): void {

    this.estadoService
      .getEstados(null)
      .subscribe(
        data => {
          this.estados = data
          console.log(data);
        },
        error => {
          console.log(error);
        }
      )

}

}
