import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistrarAutomovilComponent } from './registrar-automovil.component';

describe('RegistrarAutomovilComponent', () => {
  let component: RegistrarAutomovilComponent;
  let fixture: ComponentFixture<RegistrarAutomovilComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RegistrarAutomovilComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RegistrarAutomovilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
