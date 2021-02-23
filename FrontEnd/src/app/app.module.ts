import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WorkstationComponent } from './workstation/workstation.component';
import { ShowWorkstationComponent } from './workstation/show-workstation/show-workstation.component';
import { AddEditWorkstationComponent } from './workstation/add-edit-workstation/add-edit-workstation.component';
import {HttpClientModule} from '@angular/common/http';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {SharedService} from './shared.service';
@NgModule({
  declarations: [
    AppComponent,
    WorkstationComponent,
    ShowWorkstationComponent,
    AddEditWorkstationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
