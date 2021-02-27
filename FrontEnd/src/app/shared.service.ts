import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  getWorkstationList(): Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/workstation/');
  }
  // tslint:disable-next-line
  addWorkstation(val: any){
    return this.http.post(this.APIUrl + '/workstation/', val);
  }

  // tslint:disable-next-line
  updateWorkstation(val: any){
    return this.http.put(this.APIUrl + '/workstation/', val);
  }

  // tslint:disable-next-line
  deleteWorkstation(val: any){
    return this.http.delete(this.APIUrl + '/workstation/', val);
  }
}
