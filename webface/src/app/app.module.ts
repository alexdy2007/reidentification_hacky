import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {MdCardModule} from '@angular/material';

import { AppComponent } from './app.component';
import { VisableComponent } from './visable/visable.component';
import { AlertModule } from 'ngx-bootstrap';

import { AppRoutingModule }     from './app-routing.module';
import { PersonComponent } from './person/person.component';
import { HttpModule }    from '@angular/http';
import {DataTableModule} from "angular2-datatable";
import {PersonFilterPipe} from "./person/personfilter";


@NgModule({
  declarations: [
    AppComponent,
    VisableComponent,
    PersonComponent,
    PersonFilterPipe
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    NgbModule.forRoot(),
    AlertModule.forRoot(),
    MdCardModule,
    AppRoutingModule,
    HttpModule,
    DataTableModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
