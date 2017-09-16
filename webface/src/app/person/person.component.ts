import { Component, OnInit } from '@angular/core';
import {PersonService} from "../service/person-service";
import {Observable} from "rxjs/Rx";
import { Subject }           from 'rxjs/Subject';
import { Person }           from '../person/person';


@Component({
  selector: 'person',
  templateUrl: './person.component.html',
  styleUrls: ['./person.component.css'],
  providers: [PersonService]

})
export class PersonComponent implements OnInit {

    public data;
    public selectedHero: Person;
    public filterQuery = "";
    public rowsOnPage = 10;
    public sortBy = "email";
    public sortOrder = "asc";

  constructor(
     private personService: PersonService) {

     personService.newpersonDataAnnounced$.subscribe(
          data => {
            this.data = data
          }
      );

  }

  getPersons(): void {
    this.personService.getPersonData();
  }

  ngOnInit() : void {
    this.getPersons();
  }

}
