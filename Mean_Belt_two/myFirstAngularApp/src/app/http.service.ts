import { Injectable } from '@angular/core';
import {HttpClient} from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
 pass_object=null;
 constructor(private _http: HttpClient) { 



  }

  allObjects(){
 
    return this._http.get('/objects'); 
  } 

  createObject(newObject){
 
      return this._http.post('/objects', newObject);
  }

  showThisObject(id){

    return this._http.get('/objects/'+id); 
  }

  updateObject(object){

    return this._http.put('/objects/'+object._id, object); 
  }

  updateOneObject(object){

    return this._http.put('/objectss/'+object._id, object); 
  }

  deleteObject(id){

    return this._http.delete('/objects/'+id); 
  }
}
