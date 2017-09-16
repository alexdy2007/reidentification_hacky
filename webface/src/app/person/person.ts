/**
 * Created by ayoung on 15/09/17.
 */

export class Person {
  public name: string;
  public role: string;
  public photo_location: string;
  public has_encoding: boolean;

  constructor(name:string, role:string, photo_location:string, has_encoding: boolean){
    this.name = name;
    this.role = role;
    this.photo_location = photo_location;
    this.has_encoding = has_encoding;
  }
}
