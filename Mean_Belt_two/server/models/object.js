// const mongoose = require('mongoose');
// const	Schema 	= mongoose.Schema;


// const CakeSchema = new mongoose.Schema({
//   baker_name: {type: String, required: true},
//   cake_url: {type: String, default: ''},
//   comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
// }, {timestamps: true});





// const Cake = mongoose.model('Cake', CakeSchema);




// module.exports = Cake;
const mongoose = require('mongoose'),
    	// bcrypt		= require('bcrypt-as-promised'),
    	// unique		= require('mongoose-unique-validator'),
    	// format      = require('format')
    	moment		= require('moment');
const Schema = mongoose.Schema;
const ObjectSchema = new mongoose.Schema({
    object_name: {
		type: String,
		trim: true,
		required: [true, "Must enter pets name"],
		 minlength: [3, "Name must be a minimum of 3 characters"],
         maxlength: [25, "Name cannot be longer than 25 characters"],
         // drop daabse
         dropDups: true
         // default: ''
	},
	object_type: {
		type: String,
		trim: true,
		required: [true, "Must enter the pets name."],
		minlength: [3, "Type must be a minimum of 3 characters"],
        maxlength: [25, "Type cannot be longer than 25 characters"]
        // default: ''
	},
    object_description: {
		type: String,
		trim: true,
		required: [true, "Must enter pets description"],
		minlength: [3, "Name must be a minimum of 3 characters"],
        maxlength: [25, "Name cannot be longer than 25 characters"],
       
	},

	skill_1: {
		type: String,
		trim: true,
		// minlength: [3, "Skill One must be a minimum of 3 characters"],
  //       maxlength: [25, "Name cannot be longer than 25 characters"],
        default: ''
      }, 
 //    birthday: {
	// 	type: Date,
	// 	required: [true, "Birthday is required"],
	// 	validate: {  // Custom Validator
	// 		validator: (value) => {
 //    			return moment().diff(value) >= 0
	// 		},
	// 		message: "Birthdate can not be a future date."
	// 	}
	// },
	skill_2: {
		type: String,
		trim: true,
		// minlength: [3, "Skill Two must be a minimum of 3 characters"],
  //       maxlength: [25, "Name cannot be longer than 25 characters"],
        default: ''
      }, 
	skill_3: {
		type: String,
		trim: true,
		// minlength: [3, "Skill Three must be a minimum of 3 characters"],
  //       maxlength: [25, "Name cannot be longer than 25 characters"],
        default: ''
      }, 
	// test: {
	// 	type: Date,
 //        default:new Date()
 //      },       
    likes: {
		type: Number,
		// minlength: [3, "Skill Three must be a minimum of 3 characters"],
  //       maxlength: [25, "Name cannot be longer than 25 characters"],
        default: 0
      }, 
	// skills: [{
	// 	type: Schema.Types.ObjectId,
	// 	ref: 'Skill',
	// 	maxlength: [3, "Pet can only have up to three skills" ]
	// }]
}, {
	timestamps: true
});
// ObjectSchema.plugin(unique, { message: "Account using '{VALUE}' already exists."});
const Object = mongoose.model('Object', ObjectSchema);
module.exports = Object;



