import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { HttpService } from '../../http.service'; 

@Component({
  selector: 'app-view2',
  templateUrl: './view2.component.html',
  styleUrls: ['./view2.component.css']
})
export class View2Component implements OnInit {
  pass_object=null;


  title = 'app';
  objects = null;
  newObject =null;
  thisObject = null;
  hidden = true;
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
    this.pass_object = this._httpService.pass_object;
    }
   
  editObject(event){
    event.preventDefault();
    let observable = this._httpService.updateObject(this.pass_object); 
    observable.subscribe(data => {     
      this.goHome();
    });
  }



goHome() {
    this._router.navigate(['/pets']);
  }
}

