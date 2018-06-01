(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ "./src/$$_lazy_route_resource lazy recursive":
/*!**********************************************************!*\
  !*** ./src/$$_lazy_route_resource lazy namespace object ***!
  \**********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error('Cannot find module "' + req + '".');
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "./src/$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "./src/app/app-routing.module.ts":
/*!***************************************!*\
  !*** ./src/app/app-routing.module.ts ***!
  \***************************************/
/*! exports provided: AppRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() { return AppRoutingModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _object_object_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./object/object.component */ "./src/app/object/object.component.ts");
/* harmony import */ var _object_view1_view1_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./object/view1/view1.component */ "./src/app/object/view1/view1.component.ts");
/* harmony import */ var _object_view2_view2_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./object/view2/view2.component */ "./src/app/object/view2/view2.component.ts");
/* harmony import */ var _object_view3_view3_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./object/view3/view3.component */ "./src/app/object/view3/view3.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};


// import { AppComponent } from '../app/app.component';




// const routes: Routes = [
//     { path: 'pets', component: ObjectComponent, children: [
//     	{ path: 'new', component: View1Component}
//         { path: ':id', component: View3Component },
//         { path: 'edit', component: View2Component }
//         ]
//     }
// ]
var routes = [
    { path: '', pathMatch: 'full', redirectTo: 'pets' },
    { path: 'pets', component: _object_object_component__WEBPACK_IMPORTED_MODULE_2__["ObjectComponent"] },
    { path: 'pets/new', component: _object_view1_view1_component__WEBPACK_IMPORTED_MODULE_3__["View1Component"] },
    { path: 'pets/:id/edit', component: _object_view2_view2_component__WEBPACK_IMPORTED_MODULE_4__["View2Component"] },
    { path: 'pets/:id', component: _object_view3_view3_component__WEBPACK_IMPORTED_MODULE_5__["View3Component"] }
];
// const routes: Routes = [
// 	{path: '', pathMatch: 'full', component: ObjectComponent },
// 	{path: 'pets', component: ObjectComponent },
// 	{path: 'pets/new', component: View1Component},
// 	{path: 'pets/:id/edit', component: View2Component},
// 	{path: 'pets/:id', component: View3Component}
// ];
var AppRoutingModule = /** @class */ (function () {
    function AppRoutingModule() {
    }
    AppRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"].forRoot(routes)],
            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"]]
        })
    ], AppRoutingModule);
    return AppRoutingModule;
}());



/***/ }),

/***/ "./src/app/app.component.css":
/*!***********************************!*\
  !*** ./src/app/app.component.css ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/app.component.html":
/*!************************************!*\
  !*** ./src/app/app.component.html ***!
  \************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n<div style=\"text-align:center\">\n\t<h1>a page</h1>\n\n<router-outlet></router-outlet>\n\n</div>\n\n\n\n\n"

/***/ }),

/***/ "./src/app/app.component.ts":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var AppComponent = /** @class */ (function () {
    function AppComponent(_route, _router) {
        this._route = _route;
        this._router = _router;
    }
    AppComponent.prototype.ngOnInit = function () {
        // this.goHome();
    };
    AppComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-root',
            template: __webpack_require__(/*! ./app.component.html */ "./src/app/app.component.html"),
            styles: [__webpack_require__(/*! ./app.component.css */ "./src/app/app.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["ActivatedRoute"],
            _angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], AppComponent);
    return AppComponent;
}());



/***/ }),

/***/ "./src/app/app.module.ts":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/fesm5/platform-browser.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
/* harmony import */ var _http_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./http.service */ "./src/app/http.service.ts");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
/* harmony import */ var _app_routing_module__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./app-routing.module */ "./src/app/app-routing.module.ts");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./app.component */ "./src/app/app.component.ts");
/* harmony import */ var _object_object_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./object/object.component */ "./src/app/object/object.component.ts");
/* harmony import */ var _object_view1_view1_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./object/view1/view1.component */ "./src/app/object/view1/view1.component.ts");
/* harmony import */ var _object_view2_view2_component__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./object/view2/view2.component */ "./src/app/object/view2/view2.component.ts");
/* harmony import */ var _object_view3_view3_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./object/view3/view3.component */ "./src/app/object/view3/view3.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};











var AppModule = /** @class */ (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
            declarations: [
                _app_component__WEBPACK_IMPORTED_MODULE_6__["AppComponent"],
                _object_object_component__WEBPACK_IMPORTED_MODULE_7__["ObjectComponent"],
                _object_view1_view1_component__WEBPACK_IMPORTED_MODULE_8__["View1Component"],
                _object_view2_view2_component__WEBPACK_IMPORTED_MODULE_9__["View2Component"],
                _object_view3_view3_component__WEBPACK_IMPORTED_MODULE_10__["View3Component"]
            ],
            imports: [
                _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
                _app_routing_module__WEBPACK_IMPORTED_MODULE_5__["AppRoutingModule"],
                _angular_forms__WEBPACK_IMPORTED_MODULE_4__["FormsModule"],
                _angular_common_http__WEBPACK_IMPORTED_MODULE_2__["HttpClientModule"]
            ],
            providers: [_http_service__WEBPACK_IMPORTED_MODULE_3__["HttpService"]],
            bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_6__["AppComponent"]]
        })
    ], AppModule);
    return AppModule;
}());



/***/ }),

/***/ "./src/app/http.service.ts":
/*!*********************************!*\
  !*** ./src/app/http.service.ts ***!
  \*********************************/
/*! exports provided: HttpService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HttpService", function() { return HttpService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var HttpService = /** @class */ (function () {
    function HttpService(_http) {
        this._http = _http;
        this.pass_object = null;
    }
    HttpService.prototype.allObjects = function () {
        return this._http.get('/objects');
    };
    HttpService.prototype.createObject = function (newObject) {
        return this._http.post('/objects', newObject);
    };
    HttpService.prototype.showThisObject = function (id) {
        return this._http.get('/objects/' + id);
    };
    HttpService.prototype.updateObject = function (object) {
        return this._http.put('/objects/' + object._id, object);
    };
    HttpService.prototype.updateOneObject = function (object) {
        return this._http.put('/objectss/' + object._id, object);
    };
    HttpService.prototype.deleteObject = function (id) {
        return this._http.delete('/objects/' + id);
    };
    HttpService = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"])({
            providedIn: 'root'
        }),
        __metadata("design:paramtypes", [_angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"]])
    ], HttpService);
    return HttpService;
}());



/***/ }),

/***/ "./src/app/object/object.component.css":
/*!*********************************************!*\
  !*** ./src/app/object/object.component.css ***!
  \*********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\r\n/*for Main Form*/\r\n#capitalize {\r\n text-transform: capitalize;\r\n}\r\n#container{\r\n\r\n\t\r\n}\r\nform{\r\n\tdisplay: inline-block;\r\n\tvertical-align: top;\r\n\tborder:solid;\r\n\tborder-color: black;\r\n\twidth: 400px;\r\n\theight:300px;\r\n\tmargin-left: 100px;\r\n\r\n\t}\r\n.form_row {\r\n\tmargin-top: 5px;\r\n\tdisplay: flex;\r\n}\r\n.form_row label {\r\n  display: inline-block;\r\n  width: 75px;\r\n  margin-right:10px;\r\n  flex:1;\r\n}\r\n.form_row input{\r\n\tflex:6;\r\n\t\r\n}\r\n.form_row select{\r\nflex:1;\r\nmargin-left: 10px;\r\n\r\n}\r\n#password_notice{\r\n\tfont-size: 10px;\r\n}\r\ninput{\r\n\tmax-height: 15px;\r\n\tmax-width: 200px;\r\n}\r\n#register{\r\n\tmax-height: 30px;\r\n\tmax-width: 100px;\r\n\tmargin-left: 173px;\r\n}\r\n/*For Rows*/\r\ntable {\r\n    font-family: arial, sans-serif;\r\n    border-collapse: collapse;\r\n    width: 50%;\r\n}\r\ntd, th {\r\n    border: 1px solid #dddddd;\r\n    text-align: left;\r\n    padding: 8px;\r\n}\r\ntr {\r\n\t    border: solid;\r\n    border-color: black;\r\n}\r\ntr:nth-child(odd) {\r\n    background-color: #dddddd;\r\n}\r\ntd, button{\r\n\tmargin-left: 9px;\r\n}"

/***/ }),

/***/ "./src/app/object/object.component.html":
/*!**********************************************!*\
  !*** ./src/app/object/object.component.html ***!
  \**********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<h1>Pet Shelter</h1>  \n\n<a [routerLink]=\"['/pets/new']\">Add A Pet!</a> \n\n\n  <div id='object_table'>\n    <table>\n      <tr>\n        <th>Name</th>\n        <th>Type</th>\n        <th>Created At</th>\n        <th>Actions</th>\n\n      </tr>\n      <tr *ngFor= \"let object of objects\">\n        <td>{{object.object_name}}</td>\n        <td>{{object.object_type}}</td>\n        <!-- angular format date -->\n        <td>{{object.createdAt | date:'MMM, dd, yyyy'}}</td>\n        <!-- https://docs.angularjs.org/api/ng/filter/date -->\n        <!-- <td>{{object.createdAt | date:'MM/dd/yyyy @ h:mma'}}</td> -->\n        <td> <a (click)=\"details(object)\" [routerLink]=\"['/pets',object._id]\"><button>Pet Details</button></a>  <a (click)=\"edit(object)\" [routerLink]=\"['/pets',object._id,'edit']\"><button>Edit Pet</button></a> </td>\n      </tr>\n    </table>\n  </div>\n\n<!-- [routerLink]=\"['/pets',object._id]\" -->\n"

/***/ }),

/***/ "./src/app/object/object.component.ts":
/*!********************************************!*\
  !*** ./src/app/object/object.component.ts ***!
  \********************************************/
/*! exports provided: ObjectComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ObjectComponent", function() { return ObjectComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _http_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../http.service */ "./src/app/http.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var ObjectComponent = /** @class */ (function () {
    function ObjectComponent(_httpService) {
        this._httpService = _httpService;
        this.title = 'app';
        this.pass_object = null;
        this.objects = null;
        this.newObject = null;
        this.thisObject = null;
        this.hidden = true;
        this.thisObjectComments = null;
        this.starAvg = null;
        this.objectComment = null;
        this.newObject = { object_name: '', object_type: '', object_description: '', skill_1: '', skill_2: '', skill_3: '' };
        this.thisObject = { object_name: '', object_type: '', object_description: '', skill_1: '', skill_2: '', skill_3: '' };
    }
    ObjectComponent.prototype.ngOnInit = function () {
        this.allObjects();
    };
    ObjectComponent.prototype.allObjects = function () {
        var _this = this;
        var observable = this._httpService.allObjects();
        observable.subscribe(function (data) {
            _this.objects = data;
            // console.log(data[0].likes+1.33)
        });
    };
    ObjectComponent.prototype.makeObject = function (event) {
        var _this = this;
        event.preventDefault();
        var observable = this._httpService.createObject(this.newObject);
        observable.subscribe(function (data) {
            _this.allObjects();
        });
    };
    ObjectComponent.prototype.edit = function (object) {
        this._httpService.pass_object = object;
    };
    ObjectComponent.prototype.details = function (object) {
        this._httpService.pass_object = object;
    };
    ObjectComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-object',
            template: __webpack_require__(/*! ./object.component.html */ "./src/app/object/object.component.html"),
            styles: [__webpack_require__(/*! ./object.component.css */ "./src/app/object/object.component.css")]
        }),
        __metadata("design:paramtypes", [_http_service__WEBPACK_IMPORTED_MODULE_1__["HttpService"]])
    ], ObjectComponent);
    return ObjectComponent;
}());



/***/ }),

/***/ "./src/app/object/view1/view1.component.css":
/*!**************************************************!*\
  !*** ./src/app/object/view1/view1.component.css ***!
  \**************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\r\n/*for Main Form*/\r\n#capitalize {\r\n text-transform: capitalize;\r\n}\r\n#container{\r\n\r\n\t\r\n}\r\nform{\r\n\tdisplay: inline-block;\r\n\tvertical-align: top;\r\n\tborder:solid;\r\n\tborder-color: black;\r\n\twidth: 400px;\r\n\theight:300px;\r\n\tmargin-left: 100px;\r\n\r\n\t}\r\n.form_row {\r\n\tmargin-top: 5px;\r\n\tdisplay: flex;\r\n}\r\n.form_row label {\r\n  display: inline-block;\r\n  width: 75px;\r\n  margin-right:10px;\r\n  flex:1;\r\n}\r\n.form_row input{\r\n\tflex:6;\r\n\t\r\n}\r\n.form_row select{\r\nflex:1;\r\nmargin-left: 10px;\r\n\r\n}\r\ninput{\r\n\tmax-height: 15px;\r\n\tmax-width: 200px;\r\n}\r\n#register{\r\n\tmax-height: 30px;\r\n\tmax-width: 100px;\r\n\tmargin-left: 173px;\r\n}\r\nlabel{\r\n\tdisplay: block;\r\n}\r\n/*For Rows*/\r\ntable {\r\n    font-family: arial, sans-serif;\r\n    border-collapse: collapse;\r\n    width: 50%;\r\n}\r\ntd, th {\r\n    border: 1px solid #dddddd;\r\n    text-align: left;\r\n    padding: 8px;\r\n}\r\ntr {\r\n\t    border: solid;\r\n    border-color: black;\r\n}\r\ntr:nth-child(odd) {\r\n    background-color: #dddddd;\r\n}\r\ntd, button{\r\n\tmargin-left: 9px;\r\n}"

/***/ }),

/***/ "./src/app/object/view1/view1.component.html":
/*!***************************************************!*\
  !*** ./src/app/object/view1/view1.component.html ***!
  \***************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<h1>Pet Shelter</h1>\n\n<div id='container'>\n  <form (submit)=\"makeObject($event)\">\n<!--     <p> {{ newObject| json }} </p> -->\n    <div class=\"form_row\">\n      <label for='name'>Object Name</label>\n      <input type=\"text\" name=\"name\" [(ngModel)]=\"newObject.object_name\" #name=\"ngModel\"   required minlength=\"3\" maxlength=\"20\"/> \n      <small *ngIf=\"name.invalid\">Name must be present and longer than 3 characters</small>\n      <!-- {{bakerName.errors | json }} -->\n    </div>\n\n    <div class=\"form_row\">\n      <label for='type'>Object Type</label>\n      <input id='capitalize' type=\"text\" name=\"type\" [(ngModel)]=\"newObject.object_type\" #type=\"ngModel\" required minlength=\"2\" maxlength=\"12\"/>\n      <small *ngIf=\"type.invalid\">Type must be present and longer than 3 characters</small> \n    </div>\n\n    <div class=\"form_row\">\n      <label for='description'>Description</label>\n      <input type=\"text\" name=\"description\" [(ngModel)]=\"newObject.object_description\" #description=\"ngModel\" required minlength=\"2\" maxlength=\"12\"/> \n      <small *ngIf=\"description.invalid\">Description must be present and longer than 3 characters</small>\n    </div>\n\n    <h4>Skills</h4>\n    <div class=\"form_row\">\n      <label for='skill1'>Skill 1:</label>\n      <input type=\"text\" name=\"skill1\" [(ngModel)]=\"newObject.skill_1\" />\n    </div>  \n\n    <div class=\"form_row\">\n      <label for='skill2'>Skill 2:</label>\n      <input type=\"text\" name=\"skill2\" [(ngModel)]=\"newObject.skill_2\" />\n    </div>  \n\n\n    <div class=\"form_row\">\n      <label for='skill3'>Skill 3:</label>\n      <input type=\"text\" name=\"skill3\" [(ngModel)]=\"newObject.skill_3\"/>\n    </div>  \n\n      <div class=\"form_row\" >\n         <input type='submit' value='Add Pet' id=\"register\"/>\n         <a  [routerLink]=\"['/pets']\"><button>Back</button></a>\n     </div>  \n\n     <small *ngIf=\"user_err_message\">Name Is Taken</small>\n\n  </form>\n\n"

/***/ }),

/***/ "./src/app/object/view1/view1.component.ts":
/*!*************************************************!*\
  !*** ./src/app/object/view1/view1.component.ts ***!
  \*************************************************/
/*! exports provided: View1Component */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "View1Component", function() { return View1Component; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _http_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../http.service */ "./src/app/http.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var View1Component = /** @class */ (function () {
    function View1Component(_httpService, _route, _router) {
        this._httpService = _httpService;
        this._route = _route;
        this._router = _router;
        this.title = 'app';
        this.user_err = null;
        this.user_err_message = null;
        this.pass_object = null;
        this.objects = null;
        this.newObject = null;
        this.thisObject = null;
        this.hidden = true;
        this.thisObjectComments = null;
        this.starAvg = null;
        this.objectComment = null;
        this.newObject = { object_name: '', object_type: '', object_description: '', skill_1: '', skill_2: '', skill_3: '' };
        this.thisObject = { object_name: '', object_type: '', object_description: '', skill_1: '', skill_2: '', skill_3: '' };
    }
    View1Component.prototype.ngOnInit = function () {
        this.user_err_message = false;
        this.allObjects();
    };
    View1Component.prototype.allObjects = function () {
        var _this = this;
        var observable = this._httpService.allObjects();
        observable.subscribe(function (data) {
            _this.objects = data;
            console.log(data);
        });
    };
    View1Component.prototype.makeObject = function (event) {
        var _this = this;
        event.preventDefault();
        var observable = this._httpService.createObject(this.newObject);
        observable.subscribe(function (data) {
            _this.allObjects();
            console.log(data);
            if (data == 'object already exists') {
                _this.user_err_message = true;
            }
            else {
                _this.goHome();
            }
        });
    };
    View1Component.prototype.goHome = function () {
        this._router.navigate(['/pets']);
    };
    View1Component = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-view1',
            template: __webpack_require__(/*! ./view1.component.html */ "./src/app/object/view1/view1.component.html"),
            styles: [__webpack_require__(/*! ./view1.component.css */ "./src/app/object/view1/view1.component.css")]
        }),
        __metadata("design:paramtypes", [_http_service__WEBPACK_IMPORTED_MODULE_2__["HttpService"], _angular_router__WEBPACK_IMPORTED_MODULE_1__["ActivatedRoute"],
            _angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], View1Component);
    return View1Component;
}());



/***/ }),

/***/ "./src/app/object/view2/view2.component.css":
/*!**************************************************!*\
  !*** ./src/app/object/view2/view2.component.css ***!
  \**************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "#container{\r\n\tmargin: 0 auto;\r\n\tmax-width: 450px;\r\n\tborder-color: blue;\r\n\tborder:solid;\r\n}\r\n\r\ninput{\r\n\tborder-radius: 5px;\r\n\twidth:400px;\r\n}\r\n\r\nh4{\r\n\ttext-align: left;\r\n\twidth:330px;\r\n\tmargin-bottom: -2px;\r\n}\r\n\r\n.form_row{\r\n\tmax-width: 400px;\r\n}\r\n\r\n.input2{\r\n\tborder-radius: 5px;\r\n\twidth:325px;\r\n}\r\n\r\n.skill_row{\r\n\tmargin-left: 20px;\r\n\tmargin-top: 5px;\r\n\tmargin-bottom: 5px;\r\n}\r\n\r\nlabel{\r\n\tmargin-right:5px;\r\n}\r\n\r\n.input3{\r\n\theight: 25px;\r\n\twidth: 75px;\r\n\tborder-radius: 5px;\r\n\tcolor:white;\r\n\tbackground-color: lightblue;\r\n}"

/***/ }),

/***/ "./src/app/object/view2/view2.component.html":
/*!***************************************************!*\
  !*** ./src/app/object/view2/view2.component.html ***!
  \***************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div id='container'>\n  <form (submit)=\"editObject($event)\" >\n<!--     <p> {{ pass_object| json }} </p> -->\n\n    <div class=\"form_row\">\n      <h4 for='name'>Object Name</h4>\n      <input  type=\"text\" name=\"name\" [(ngModel)]=\"pass_object.object_name\" #name=\"ngModel\" value=\"pass_object.object_name\"  required minlength=\"3\" maxlength=\"20\"/> \n      <small *ngIf=\"name.invalid\">Name must be present and longer than 3 characters</small>\n      <!-- {{bakerName.errors | json }} -->\n    </div>\n\n    <div class=\"form_row\">\n      <h4 for='type'>Object Type</h4>\n      <input id='capitalize' type=\"text\" name=\"type\" [(ngModel)]=\"pass_object.object_type\" #type=\"ngModel\" value=\"pass_object.object_type\" required minlength=\"2\" maxlength=\"12\"/>\n      <small *ngIf=\"name.invalid\">Type must be present and longer than 3 characters</small> \n    </div>\n\n    <div class=\"form_row\">\n      <h4 for='description'>Description</h4>\n      <input type=\"text\" name=\"description\" [(ngModel)]=\"pass_object.object_description\" #description=\"ngModel\" value=\"pass_object.object_description\" required minlength=\"2\" maxlength=\"12\"/> \n      <small *ngIf=\"description.invalid\">Description must be present and longer than 3 characters</small>\n    </div>\n\n    <h4>Skills</h4>\n    <div class=\"form_row skill_row\" >\n      <label for='skill1'>Skill 1:</label>\n      <input class='input2' type=\"text\" name=\"skill1\" [(ngModel)]=\"pass_object.skill_1\" value=\"pass_object.skill_1\"/>\n    </div>  \n\n    <div class=\"form_row skill_row\" >\n      <label for='skill2'>Skill 2:</label>\n      <input class='input2' type=\"text\" name=\"skill2\" [(ngModel)]=\"pass_object.skill_2\" value=\"pass_object.skill_2\"/>\n    </div>  \n\n\n    <div class=\"form_row skill_row\" >\n      <label for='skill3'>Skill 3:</label>\n      <input class='input2' type=\"text\" name=\"skill3\" [(ngModel)]=\"pass_object.skill_3\" value=\"pass_object.skill_3\"/>\n    </div>  \n\n      <div class=\"form_row\" >\n         <input class='input3' type='submit' value='Update' id=\"register\" />\n         <a  [routerLink]=\"['/pets']\"><button class='input3'>Cancel</button></a>\n     </div>  \n\n  </form>\n\n</div>\n"

/***/ }),

/***/ "./src/app/object/view2/view2.component.ts":
/*!*************************************************!*\
  !*** ./src/app/object/view2/view2.component.ts ***!
  \*************************************************/
/*! exports provided: View2Component */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "View2Component", function() { return View2Component; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _http_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../http.service */ "./src/app/http.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var View2Component = /** @class */ (function () {
    // use this when not using routing to pass infomation to a component
    // @Input() cakes;      
    //   @Input() newCake;
    //   @Input() thisCake;
    //   @Input() hidden;
    //   @Input() thisCakeComments;
    //   @Input() starAvg;  
    //   @Input() cakeComment;
    function View2Component(_httpService, _route, _router) {
        this._httpService = _httpService;
        this._route = _route;
        this._router = _router;
        this.pass_object = null;
        this.title = 'app';
        this.objects = null;
        this.newObject = null;
        this.thisObject = null;
        this.hidden = true;
        this.thisObjectComments = null;
        this.starAvg = null;
        this.objectComment = null;
        this.newObject = { object_name: '', object_type: '', object_description: '', skill_1: '', skill_2: '', skill_3: '' };
        this.thisObject = { object_name: '', object_type: '', object_description: '', skill_1: '', skill_2: '', skill_3: '' };
    }
    View2Component.prototype.ngOnInit = function () {
        this.pass_object = this._httpService.pass_object;
    };
    View2Component.prototype.editObject = function (event) {
        var _this = this;
        event.preventDefault();
        var observable = this._httpService.updateObject(this.pass_object);
        observable.subscribe(function (data) {
            _this.goHome();
        });
    };
    View2Component.prototype.goHome = function () {
        this._router.navigate(['/pets']);
    };
    View2Component = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-view2',
            template: __webpack_require__(/*! ./view2.component.html */ "./src/app/object/view2/view2.component.html"),
            styles: [__webpack_require__(/*! ./view2.component.css */ "./src/app/object/view2/view2.component.css")]
        }),
        __metadata("design:paramtypes", [_http_service__WEBPACK_IMPORTED_MODULE_2__["HttpService"], _angular_router__WEBPACK_IMPORTED_MODULE_1__["ActivatedRoute"],
            _angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], View2Component);
    return View2Component;
}());



/***/ }),

/***/ "./src/app/object/view3/view3.component.css":
/*!**************************************************!*\
  !*** ./src/app/object/view3/view3.component.css ***!
  \**************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "#container{\r\n\r\n}\r\n#details-container{\r\n\tmargin: 0 auto;\r\n\r\n\tmax-width: 500px;\r\n\tborder: solid;\r\n\tborder-color: black;\r\n\ttext-align: center;\r\n}\r\n#heading{\r\n\tmax-width: 500px;\r\n\tborder: solid;\r\n\tborder-color: black;\r\n}\r\n#header{\r\n\tdisplay: inline-block;\r\n}\r\n#home{\r\n\tmargin-left: 100px;\r\n\tdisplay: inline-block;\r\n\tborder: solid;\r\n\tmargin\r\n\tborder-color: black;\r\n}\r\n.row{\r\n\tdisplay: block;\r\n\tmax-width: 500px;\r\n}\r\n.title{\r\n\tmargin-left: 0;\r\n\tvertical-align: center;\r\n\tmin-width:200px;\r\n\tdisplay: inline-block;\r\n}\r\n.data{\r\n\ttext-align: left;\r\n\tmin-width:300px;\r\n\tvertical-align: center;\r\n\tdisplay: inline-block;\r\n}"

/***/ }),

/***/ "./src/app/object/view3/view3.component.html":
/*!***************************************************!*\
  !*** ./src/app/object/view3/view3.component.html ***!
  \***************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div id='container'>\n\t<div id='details-container'>\n\n\t\t<div id='heading'>\n\t\t\t<h1 id='header'>Pet Shelter</h1>\n\t\t\t<a  [routerLink]=\"['/pets']\" id='home'>Home</a>\n\t\t</div>\n\t\t<h2>Details about {{pass_object.object_name}} </h2>\n\n\t\t<div class='row'>\n\t\t\t<h4 class='title'>Pet Type:</h4>\n\t\t\t<p class='data'>{{pass_object.object_type}}</p>\n\t\t</div>\n\n\t\t<div class='row'>\n\t\t\t<h4 class='title'>Pet Description:</h4>\n\t\t\t<p class='data'>{{pass_object.object_description}}</p>\n\t\t</div>\n\n\t\t<div class='row'>\n\t\t\t<h4 class='title'>skills</h4>\n\t\t\t<p class='data'> {{pass_object.skill_1}}<br/>{{pass_object.skill_2}}<br/>{{pass_object.skill_3}}</p>\n\t\t</div>\n\n\t\t<div class='row'>\n\t\t\t<h4 class='title'>Likes:</h4>\n\t\t\t<p class='data'>{{pass_object.likes}} Likes</p>\n\t\t</div>\n\n\t\t<div class='row'>\n\t\t\t<a (click)=\"addLike(pass_object)\"  *ngIf=\"hidden == false\"><button>Like</button></a>\n\n\t\t\t<a (click)=\"adopt(pass_object)\" [routerLink]=\"['/pets']\"><button>Adopt</button></a>\n\t\t</div>\n\t\t<!-- [routerLink]=\"['/pets', pass_object._id]\" -->\n\t</div>\n</div>\n\n"

/***/ }),

/***/ "./src/app/object/view3/view3.component.ts":
/*!*************************************************!*\
  !*** ./src/app/object/view3/view3.component.ts ***!
  \*************************************************/
/*! exports provided: View3Component */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "View3Component", function() { return View3Component; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _http_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../http.service */ "./src/app/http.service.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var View3Component = /** @class */ (function () {
    // use this when not using routing to pass infomation to a component
    // @Input() cakes;      
    //   @Input() newCake;
    //   @Input() thisCake;
    //   @Input() hidden;
    //   @Input() thisCakeComments;
    //   @Input() starAvg;  
    //   @Input() cakeComment;
    function View3Component(_httpService, _route, _router) {
        this._httpService = _httpService;
        this._route = _route;
        this._router = _router;
        this.pass_object = null;
        this.title = 'app';
        this.objects = null;
        this.newObject = null;
        this.thisObject = null;
        this.hidden = null;
        this.thisObjectComments = null;
        this.starAvg = null;
        this.objectComment = null;
        this.newObject = { object_name: '', object_type: '', object_description: '', skill_1: '', skill_2: '', skill_3: '' };
        this.thisObject = { object_name: '', object_type: '', object_description: '', skill_1: '', skill_2: '', skill_3: '' };
    }
    View3Component.prototype.ngOnInit = function () {
        this.hidden = false;
        this.pass_object = this._httpService.pass_object;
    };
    View3Component.prototype.adopt = function (object) {
        var _this = this;
        var observable = this._httpService.deleteObject(object._id);
        observable.subscribe(function (data) {
            _this.goHome();
        });
    };
    View3Component.prototype.goHome = function () {
        this._router.navigate(['/pets']);
    };
    View3Component.prototype.addLike = function (object) {
        var _this = this;
        var observable = this._httpService.updateOneObject(object);
        this.hidden = true;
        observable.subscribe(function (data) {
            _this.pass_object = data;
        });
    };
    View3Component = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-view3',
            template: __webpack_require__(/*! ./view3.component.html */ "./src/app/object/view3/view3.component.html"),
            styles: [__webpack_require__(/*! ./view3.component.css */ "./src/app/object/view3/view3.component.css")]
        }),
        __metadata("design:paramtypes", [_http_service__WEBPACK_IMPORTED_MODULE_2__["HttpService"], _angular_router__WEBPACK_IMPORTED_MODULE_1__["ActivatedRoute"],
            _angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], View3Component);
    return View3Component;
}());



/***/ }),

/***/ "./src/environments/environment.ts":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build ---prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
var environment = {
    production: false
};
/*
 * In development mode, to ignore zone related error stack frames such as
 * `zone.run`, `zoneDelegate.invokeTask` for easier debugging, you can
 * import the following file, but please comment it out in production mode
 * because it will have performance impact when throw error
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "./src/main.ts":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser-dynamic */ "./node_modules/@angular/platform-browser-dynamic/fesm5/platform-browser-dynamic.js");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "./src/app/app.module.ts");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./environments/environment */ "./src/environments/environment.ts");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_3__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
}
Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(function (err) { return console.log(err); });


/***/ }),

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! C:\Users\BroBoFett\Desktop\Mean_Belt_two\myFirstAngularApp\src\main.ts */"./src/main.ts");


/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map