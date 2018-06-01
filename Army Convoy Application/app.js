
const createVehicle = document.getElementById('add-vehicle-button-container');
const vehicleList = document.getElementById('vehicle-list');
const assignSoldiers=document.getElementById('vehicle-list');
const delbutton=document.getElementById('soldier-name_');
const print = document.getElementById("print");
var x=3;





createVehicle.addEventListener('click', (e)=>{
    if(e.target.id === 'button' && x!==19){
    	x++;
    	const li=document.createElement("LI");
    	const ul=document.getElementById("vehicle-list");
    	li.setAttribute("id","vehicle"+x+"");
    	li.setAttribute("class","flex-container");
    	const content="<div id='actual-vehicle' class='flex-container'><div id='upper-half' class='flex-container'><div id='vehicle-picture' class='flex-container'><img src='HMMWV.jpg' height='90' width='200'></div><div id='detailed-info-fields' class='flex-container'><input type='text' name='name' id='vehicle-type"+x+"' placeholder='Vehicle Type'><input type='text' name='name' id='call-sign"+x+"' placeholder='Call Sign'><input type='text' name='name' id='serial-number"+x+"' placeholder='Serial Number'><input type='text' name='name' id='order-submit"+x+"' placeholder='Order of Movement Number'></div></div><div id='assign-soldiers' class='flex-container'><button type='button' id='button"+x+"' class='button2'>Click To Assign Soldier</button><input type='text' name='name' id='submit"+x+"' placeholder='Soldier Name/Position'><ol class='flex-container' id='soldier-name"+x+"'></ol><button type='button' id='delete-vehicle' class='button3'>Delete Vehicle</button></div>";
    	li.innerHTML=content;
    	ul.append(li);
    }
});
createVehicle.addEventListener('click', (e)=>{ 
  if (e.target.id === 'delete-button') {
    const li = e.target.parentNode;
    const ul = li.parentNode;
    ul.removeChild(li);
  }
});  

createVehicle.addEventListener('click', (e)=>{ 
  if (e.target.id === 'delete-vehicle') {
    const li = e.target.parentNode.parentNode;
    const ul = li.parentNode;
    ul.removeChild(li);
  }
});

print.addEventListener('click', (e)=>{ 
  if (e.target.id === 'print') {
  	window.print();
  }
});




// START OF WASTEFUL AND REDUNDANT CODE
createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button4' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit4');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name4');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button5' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit5');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name5');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button6' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit6');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name6');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button7' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit7');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name7');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button8' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit8');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name8');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button9' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit9');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name9');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button10' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit10');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name10');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button11' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit11');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name11');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button12' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit12');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name12');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
	 if(e.target.id === 'button13' ){
    	const li=document.createElement("LI");
    	const name=document.getElementById('submit13');
    	li.textContent=name.value;
    	const ol = document.getElementById('soldier-name13');
    	li.setAttribute("class","list-ordering");
    	console.log(name.value);
    	const btn = document.createElement('BUTTON')
    	btn.setAttribute('id',"delete-button")
    	btn.textContent="Delete"
    	li.append(btn);
    	if(name.value.length!==0){
			ol.append(li);
			name.value="";
		}
    }  

});

createVehicle.addEventListener('click', (e)=>{
     if(e.target.id === 'button14' ){
        const li=document.createElement("LI");
        const name=document.getElementById('submit14');
        li.textContent=name.value;
        const ol = document.getElementById('soldier-name14');
        li.setAttribute("class","list-ordering");
        console.log(name.value);
        const btn = document.createElement('BUTTON')
        btn.setAttribute('id',"delete-button")
        btn.textContent="Delete"
        li.append(btn);
        if(name.value.length!==0){
            ol.append(li);
            name.value="";
        }
    }  

});
createVehicle.addEventListener('click', (e)=>{
     if(e.target.id === 'button15' ){
        const li=document.createElement("LI");
        const name=document.getElementById('submit15');
        li.textContent=name.value;
        const ol = document.getElementById('soldier-name15');
        li.setAttribute("class","list-ordering");
        console.log(name.value);
        const btn = document.createElement('BUTTON')
        btn.setAttribute('id',"delete-button")
        btn.textContent="Delete"
        li.append(btn);
        if(name.value.length!==0){
            ol.append(li);
            name.value="";
        }
    }  

});
createVehicle.addEventListener('click', (e)=>{
     if(e.target.id === 'button16' ){
        const li=document.createElement("LI");
        const name=document.getElementById('submit16');
        li.textContent=name.value;
        const ol = document.getElementById('soldier-name16');
        li.setAttribute("class","list-ordering");
        console.log(name.value);
        const btn = document.createElement('BUTTON')
        btn.setAttribute('id',"delete-button")
        btn.textContent="Delete"
        li.append(btn);
        if(name.value.length!==0){
            ol.append(li);
            name.value="";
        }
    }  

});
createVehicle.addEventListener('click', (e)=>{
     if(e.target.id === 'button17' ){
        const li=document.createElement("LI");
        const name=document.getElementById('submit17');
        li.textContent=name.value;
        const ol = document.getElementById('soldier-name17');
        li.setAttribute("class","list-ordering");
        console.log(name.value);
        const btn = document.createElement('BUTTON')
        btn.setAttribute('id',"delete-button")
        btn.textContent="Delete"
        li.append(btn);
        if(name.value.length!==0){
            ol.append(li);
            name.value="";
        }
    }  

});
createVehicle.addEventListener('click', (e)=>{
     if(e.target.id === 'button18' ){
        const li=document.createElement("LI");
        const name=document.getElementById('submit18');
        li.textContent=name.value;
        const ol = document.getElementById('soldier-name18');
        li.setAttribute("class","list-ordering");
        console.log(name.value);
        const btn = document.createElement('BUTTON')
        btn.setAttribute('id',"delete-button")
        btn.textContent="Delete"
        li.append(btn);
        if(name.value.length!==0){
            ol.append(li);
            name.value="";
        }
    }  

});
createVehicle.addEventListener('click', (e)=>{
     if(e.target.id === 'button19' ){
        const li=document.createElement("LI");
        const name=document.getElementById('submit19');
        li.textContent=name.value;
        const ol = document.getElementById('soldier-name19');
        li.setAttribute("class","list-ordering");
        console.log(name.value);
        const btn = document.createElement('BUTTON')
        btn.setAttribute('id',"delete-button")
        btn.textContent="Delete"
        li.append(btn);
        if(name.value.length!==0){
            ol.append(li);
            name.value="";
        }
    }  

});

