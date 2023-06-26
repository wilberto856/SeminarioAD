import { Component, OnInit } from '@angular/core';
import { UsersService } from './users.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {

  usuarios: any;

  constructor(private userService: UsersService) { }

  ngOnInit(): void {
    this.getUsuarios();

  }

  getUsuarios(): void {

    this.userService
      .getUsuarios(null)
      .subscribe(
        data => {
          this.usuarios = data
          console.log(data);
        },
        error => {
          console.log(error);
        }
      )
  }


}
