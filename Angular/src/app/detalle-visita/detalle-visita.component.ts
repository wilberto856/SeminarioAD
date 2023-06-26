import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { VisitaService } from '../visita/visita.service';


@Component({
  selector: 'app-detalle-visita',
  templateUrl: './detalle-visita.component.html',
  styleUrls: ['./detalle-visita.component.css']
})
export class DetalleVisitaComponent implements OnInit {

  id: any;
  visita: any;

  constructor(private route: ActivatedRoute, private visitaService: VisitaService) {

  }

  ngOnInit(): void {
    this.route.
      params.subscribe(
        params =>
          this.id = params['id']
      );

    this.getVisita(this.id);

  }


  getVisita(id:any): void {

    this.visitaService
      .getVisita(id)
      .subscribe(
        data => {
          this.visita = data
          console.log(data);
        },
        error => {
          console.log(error);
        }
      )

  }



}
