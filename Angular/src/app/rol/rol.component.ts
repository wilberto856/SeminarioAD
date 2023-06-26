import { Component, OnInit } from '@angular/core';
import { RolService } from './rol.service';

@Component({
  selector: 'app-rol',
  templateUrl: './rol.component.html',
  styleUrls: ['./rol.component.css']
})
export class RolComponent implements OnInit {

  roles: any;

  constructor(private rolService: RolService) { }

  ngOnInit(): void {
    this.getRoles();
  }

  getRoles(): void {

    this.rolService
      .getRoles(null)
      .subscribe(
        data => {
          this.roles = data
          console.log(data);
        },
        error => {
          console.log(error);
        }
      )

}
}
