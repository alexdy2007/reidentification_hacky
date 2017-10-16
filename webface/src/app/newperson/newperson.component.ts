import {Component, OnInit, ViewChild} from '@angular/core';
import {FileUploader} from 'ng2-file-upload';
import {PersonService} from "../service/person-service";
import {Form, FormGroup} from "@angular/forms";

const URL : string = "http://localhost:5000/api/addperson";

@Component({
  selector: 'app-newperson',
  templateUrl: './newperson.component.html',
  styleUrls: ['./newperson.component.css'],
  providers: [PersonService]
})
export class NewpersonComponent implements OnInit {

  public person : any = {name:"", lastName:"", role:""};
  public submitted : boolean;
  public fileList: any;
  public fileName: String = "";
  public uploadStatus: any;
  private personService: PersonService;

  constructor(personService: PersonService) {
    this.personService = personService;
    this.personService.newPersonAddDataAnnounced$.subscribe(
      data => {
        this.uploadStatus = data
      }
    );
  }

  fileChange(event) {
    this.fileList = event.target.files;
    this.fileName = this.fileList[0].name;
    let a=1;
  }

  ngOnInit() {
    this.submitted = false;
    this.fileName = "";
  }


  onSubmit() {
      this.submitted = true;
      let file: File = this.fileList[0];
      let formData:FormData = new FormData();
      formData.append("name", this.person.name);
      formData.append("lastName", this.person.lastName);
      formData.append("role", this.person.role);
      formData.append('uploadFile', file, file.name);
      this.personService.uploadFile(formData).then(
        (data) => {
            console.log("Success");
        },
        (data) => {
          console.log("Failure- CORS issue most likely - could be false negative....");
        });
      this.newPerson();

  }

  newPerson() {
    this.submitted = false;
    this.person = {name:"", role:"", lastName:""};
    this.fileList = [];
    this.fileName = "";
  }

}
