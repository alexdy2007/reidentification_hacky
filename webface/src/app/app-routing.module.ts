/**
 * Created by ayoung on 15/09/17.
 */

import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { VisableComponent }   from './visable/visable.component';
import { PersonComponent }   from './person/person.component';


const routes: Routes = [
  { path: '', redirectTo: '/visable', pathMatch: 'full' },
  { path: 'visable',  component: VisableComponent, pathMatch: 'full' },
  { path: 'person',  component: PersonComponent, pathMatch: 'full' },


];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}

