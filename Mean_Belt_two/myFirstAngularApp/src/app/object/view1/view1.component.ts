import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { HttpService } from '../../http.service'; 

@Component({
  selector: 'app-view1',
  templateUrl: './view1.component.html',
  styleUrls: ['./view1.component.css']
})
export class View1Component implements OnInit {
title = 'app';
  user_err=null
  user_err_message=null
  pass_object=null;
  objects = null;
  newObject =null;
  thisObject = null;
  hidden = true;
  thisObjectComments=null;
  starAvg=null;
  objectComment=null;

  constructor(private _httpService: HttpService, private _route: ActivatedRoute,
    private _router: Router){

    this.newObject = { object_name: '', object_type: '' , object_description: '', skill_1: '' , skill_2: '', skill_3: ''};
    this.thisObject = { object_name: '', object_type: '' , object_description: '', skill_1: '' , skill_2: '', skill_3: ''};
   
  }  

  ngOnInit(){
    this.user_err_message=false;
    this.allObjects();
  }

  allObjects(){
    let observable = this._httpService.allObjects();  
    observable.subscribe(data => {     
      this.objects = data;
      console.log(data)
    });
  }

  
  makeObject(event){
    event.preventDefault();
    let observable = this._httpService.createObject(this.newObject); 
    observable.subscribe(data => {     
      this.allObjects();
      console.log(data)
      if(data == 'object already exists'){
        this.user_err_message=true;
      }
      else{
          this.goHome();
      }
     
    });
  }
  
  goHome() {
    this._router.navigate(['/pets']);
  }

  // commentOnobject(event, object){
  //   event.preventDefault();
  //   let observable = this._httpService.commentOnobject(object, this.objectComment); 
  //   observable.subscribe(data => {  
  //     console.log(data); 
  //     this.Allobjects();
  //   });
  //    this.Allobjects();
  // }

  // info(object): void {
  //   this._httpService.pass_object = object;
  // }

  // showThisobject(id){
  //   let observable = this._httpService.showThisobject(id); 
  //   this.hidden=false;
  //   observable.subscribe(data => {  
  //     console.log(data);  
  //     this.thisobject=data;
  //     this.thisobjectComments=this.thisobject.comments;
  //     for(var i=0; i<this.thisobject.comments.length; i++){
  //       this.starAvg+=this.thisobject.comments[i].stars;
  //     }
  //     this.starAvg=this.starAvg/this.thisobject.comments.length;
  //     this.starAvg = this.starAvg.toFixed(1)
  //   });

  }




