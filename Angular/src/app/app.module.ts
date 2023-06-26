import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {RouterModule, Routes} from '@angular/router';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { UsersComponent } from './users/users.component';
import {HttpClientModule} from '@angular/common/http';
import { HomeService } from './home/home.service';
import { RolComponent } from './rol/rol.component';
import { ClienteComponent } from './cliente/cliente.component';
import { EstadoComponent } from './estado/estado.component';
import { VisitaComponent } from './visita/visita.component';
import { DetalleVisitaComponent } from './detalle-visita/detalle-visita.component';
import { ClienteNuevoComponent } from './cliente-nuevo/cliente-nuevo.component';
import { FormsModule } from '@angular/forms';


const appRoute: Routes = [
  {path: '', component: HomeComponent},
  {path: '', redirectTo: 'home', pathMatch:'full'},
  {path: 'home', component: HomeComponent},
  {path: 'users', component: UsersComponent},
  {path: 'cliente', component: ClienteComponent},
  {path: 'roles', component: RolComponent},
  {path: 'estado', component: EstadoComponent},
  {path: 'visita', component: VisitaComponent},
  {path: 'detalleVisita/:id', component: DetalleVisitaComponent},
  {path: 'clientenuevo', component: ClienteNuevoComponent}
]



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    UsersComponent,
    RolComponent,
    ClienteComponent,
    EstadoComponent,
    VisitaComponent,
    DetalleVisitaComponent,
    ClienteNuevoComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(appRoute),
    FormsModule
  ],
  providers: [
    HomeService,
    UsersComponent
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
