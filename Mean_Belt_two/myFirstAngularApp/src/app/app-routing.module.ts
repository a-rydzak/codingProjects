import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// import { AppComponent } from '../app/app.component';
import { ObjectComponent } from './object/object.component';
import { View1Component } from './object/view1/view1.component';
import { View2Component } from './object/view2/view2.component';
import { View3Component } from './object/view3/view3.component';





// const routes: Routes = [
//     { path: 'pets', component: ObjectComponent, children: [
//     	{ path: 'new', component: View1Component}
//         { path: ':id', component: View3Component },
//         { path: 'edit', component: View2Component }
//         ]
//     }
// ]

const routes: Routes = [
	{path: '', pathMatch: 'full', redirectTo: 'pets' },
	{path: 'pets', component: ObjectComponent },
	{path: 'pets/new', component: View1Component},
	{path: 'pets/:id/edit', component: View2Component},
	{path: 'pets/:id', component: View3Component}
];

// const routes: Routes = [
// 	{path: '', pathMatch: 'full', component: ObjectComponent },
// 	{path: 'pets', component: ObjectComponent },
// 	{path: 'pets/new', component: View1Component},
// 	{path: 'pets/:id/edit', component: View2Component},
// 	{path: 'pets/:id', component: View3Component}
// ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
