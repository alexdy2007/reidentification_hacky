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

   //Observable Data PersonDataLust
    private personData = new BehaviorSubject(Array());
    public newpersonDataAnnounced$ = this.personData.asObservable();
  
     //Observable Data PersonDataLust
    private personVisableData = new BehaviorSubject(Array());
    public newPersonVisableDataAnnounced$ = this.personVisableData.asObservable();
  

  public getPersonData():void{
	  let query = this.dataUrl;
	  this._getData(query).subscribe(
			((res : any) =>
		 {
			 let data = res.json();
			 this.personData.next(data)
		 }).bind(this)
		);
	}
  
  public getVisableData():void{
	  let query = this.dataUrl + "/" + "peoplevisable";
	  this._getData(query).subscribe(
			((res : any) =>
		 {
			 let data = res.json();
			 this.personVisableData.next(data)
		 }).bind(this)
		);
	}
  
  
  

    private _getData(query:string): Observable<any> {
        return this.http.get(query)
    }


}
