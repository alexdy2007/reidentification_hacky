import {Injectable}     from '@angular/core';
import {Http, Response} from '@angular/http';
import {Observable}     from 'rxjs/Observable';
import {BehaviorSubject} from "rxjs/Rx";
import {Person} from "../person/person";

@Injectable()
export class PersonService {
    private dataUrl = 'http://localhost:5000/api';  // URL to web API

    constructor(private http:Http) {
    }

   //Observable Data CouncilStats
    private personData = new BehaviorSubject(Array());
    public newpersonDataAnnounced$ = this.personData.asObservable();



	  public getPersonData():void{
	  let query = this.dataUrl;
	  this._getData(query).subscribe(
			((res : any) =>
		 {
			 let data = res.json();
       let personList : Person[] = [];
       for (let i=0; i<data.length; i++){
            let p = data[i];
            personList.push(p.name, p.role, p.photo_location, p.has_encoding);
       }
       console.log("HERE");
			 this.personData.next(data)
		 }).bind(this)
		);
	}

    private _getData(query:string): Observable<any> {
        return this.http.get(query)
    }


}
