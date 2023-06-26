import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetalleVisitaComponent } from './detalle-visita.component';

describe('DetalleVisitaComponent', () => {
  let component: DetalleVisitaComponent;
  let fixture: ComponentFixture<DetalleVisitaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DetalleVisitaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetalleVisitaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
