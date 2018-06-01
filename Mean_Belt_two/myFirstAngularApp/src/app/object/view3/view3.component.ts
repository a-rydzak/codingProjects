import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { HttpService } from '../../http.service'; 

@Component({
  selector: 'app-view3',
  templateUrl: './view3.component.html',
  styleUrls: ['./view3.component.css']
})
export class View3Component implements OnInit {
pass_object=null;

  title = 'app';
  objects = null;
  newObject =null;
  thisObject = null;
  hidden = null;
  thisObjectComments=null;
  starAvg=null;
  objectComment=null;

  // use this when not using routing to pass infomation to a component
// @Input() cakes;      
//   @Input() newCake;
//   @Input() thisCake;
//   @Input() hidden;
//   @Input() thisCakeComments;
//   @Input() starAvg;  
//   @Input() cakeComment;

 constructor(private _httpService: HttpService, private _route: ActivatedRoute,
    private _router: Router){  
 	this.newObject = { object_name: '', object_type: '' , object_description: '', skill_1: '' , skill_2: '', skill_3: ''};
    this.thisObject = { object_name: '', object_type: '' , object_description: '', skill_1: '' , skill_2: '', skill_3: ''};
 }  


  ngOnInit() {
  	this.hidden=false;
    this.pass_object = this._httpService.pass_object;
    }
   
  adopt(object){
    let observable = this._httpService.deleteObject(object._id); 
    observable.subscribe(data => {     
      this.goHome();
    });
  }

  goHome() {
    this._router.navigate(['/pets']);
  }

addLike(object){
    let observable = this._httpService.updateOneObject(object); 
    this.hidden=true;
    observable.subscribe(data => {
      this.pass_object=data;        
    });
  }



// refresh() {
//     this._router.navigate(['/pets/'+pass_object._id]);
//   }
}
