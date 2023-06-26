import { Component, OnInit } from '@angular/core';
import { VisitaService } from './visita.service';

@Component({
  selector: 'app-visita',
  templateUrl: './visita.component.html',
  styleUrls: ['./visita.component.css']
})
export class VisitaComponent implements OnInit {

  visitas: any;

  constructor(private visitaService: VisitaService) { }

  ngOnInit(): void {
    this.getVisitas();

  }

  getVisitas(): void {

    this.visitaService
      .getVisitas(null)
      .subscribe(
        data => {
          this.visitas = data
          console.log(data);
        },
        error => {
          console.log(error);
        }
      )

}
}
