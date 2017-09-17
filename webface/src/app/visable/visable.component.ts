import { Component, OnInit } from '@angular/core';
import {PersonService} from "../service/person-service";
import {IntervalObservable} from "rxjs/observable/IntervalObservable"


@Component({
  selector: 'visable',
  templateUrl: './visable.component.html',
  styleUrls: ['./visable.component.css'],
  providers: [PersonService]
})
export class VisableComponent implements OnInit {

  private personService: PersonService;
  private peoplevis: any;
  private poll : boolean

  constructor(personService: PersonService) {
    this.peoplevis = [];
    this.personService = personService;
    this.personService.newPersonVisableDataAnnounced$.subscribe(
      data => {
        console.log("CALL MADE");
        this.peoplevis = data
      }
    );
  }

  getVisablePeople():void {
    this.personService.getVisableData()
  }


  ngOnInit() {
    this.poll = true;
      IntervalObservable.create(3000).takeWhile(() => this.poll).subscribe(() => this.getVisablePeople());
  }

  ngOnDestroy(){
    this.poll = false
  }

}
