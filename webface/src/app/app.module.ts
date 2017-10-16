import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FormBuilder, FormControl, FormGroup, FormsModule, Validators} from '@angular/forms';

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {MatCardModule} from '@angular/material';
import { FileSelectDirective } from 'ng2-file-upload';


import { AppComponent } from './app.component';
import { AlertModule } from 'ngx-bootstrap';

import { AppRoutingModule }     from './app-routing.module';
import { HttpModule }    from '@angular/http';
import {DataTableModule} from "angular2-datatable";
import {PersonFilterPipe} from "./person/personfilter";

import { VisableComponent } from './visable/visable.component';
import { NewpersonComponent } from './newperson/newperson.component';
import { PersonComponent } from './person/person.component';


@NgModule({
  declarations: [
    AppComponent,
    VisableComponent,
    PersonComponent,
    PersonFilterPipe,
    NewpersonComponent,
    FileSelectDirective
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    NgbModule.forRoot(),
    AlertModule.forRoot(),
    MatCardModule,
    AppRoutingModule,
    HttpModule,
    DataTableModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
