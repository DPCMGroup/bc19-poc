import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowWorkstationComponent } from './show-workstation.component';

describe('ShowWorkstationComponent', () => {
  let component: ShowWorkstationComponent;
  let fixture: ComponentFixture<ShowWorkstationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowWorkstationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ShowWorkstationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
