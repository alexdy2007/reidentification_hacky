import {Injectable} from '@angular/core';
import {Http, RequestOptions, Response, Headers} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import {BehaviorSubject} from "rxjs/Rx";
import {Person} from "../person/person";
import 'rxjs/add/operator/share';

@Injectable()
export class PersonService {
  private dataUrl = 'http://localhost:5000/api';  // URL to web API

  constructor(private http: Http) {
  }

  //Observable Data PersonDataLust
  private personData = new BehaviorSubject(Array());
  public newpersonDataAnnounced$ = this.personData.asObservable();

  //Observable Data PersonDataLust
  private personVisableData = new BehaviorSubject(Array());
  public newPersonVisableDataAnnounced$ = this.personVisableData.asObservable();


  //Observable Data AddPerson
  private personAddData = new BehaviorSubject(Array());
  public newPersonAddDataAnnounced$ = this.personAddData.asObservable();


  public getPersonData(): void {
    let query = this.dataUrl;
    this._getData(query).subscribe(
      ((res: any) => {
        let data = res.json();
        this.personData.next(data)
      }).bind(this)
    );
  }

  public getVisableData(): void {
    let query = this.dataUrl + "/" + "peoplevisable";
    this._getData(query).subscribe(
      ((res: any) => {
        let data = res.json();
        this.personVisableData.next(data)
      }).bind(this)
    );
  }

  public uploadFile(formData:FormData):Promise<any> {
      let url = this.dataUrl + "/" + "addperson";
      return new Promise((resolve, reject) => {

          let xhr:XMLHttpRequest = new XMLHttpRequest();
          xhr.open('POST', url, true);
          //xhr.setRequestHeader('Access-Control-Allow-Origin', 'http://localhost:4200');
          xhr.onreadystatechange = () => {
              if (xhr.readyState === 4) {
                  if (xhr.status === 200) {
                      resolve(<any>JSON.parse(xhr.response));
                  } else {
                      reject(xhr.response);
                  }
              }
          };



          xhr.send(formData);
      });
  }


  private _getData(query: string): Observable<any> {
    return this.http.get(query)
  }

  private _postData(url: string, options: RequestOptions, formData: FormData): Observable<any> {
    return this.http.post(url, formData, options)
  }


}
