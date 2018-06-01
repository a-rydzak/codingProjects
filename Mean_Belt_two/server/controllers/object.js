const mongoose = require('mongoose');
var Object = require('../models/object.js');
// var Comment = require('../models/comment.js');


module.exports = {
 showAll: (req, res) => {
    // Object.find({}, (err, object) => {
      Object.find({}).sort('createdAt').exec(function(err, object) { 
      if (err) {
        res.json(err);
      }
      else {
        res.json(object);
      }
    })
  },
  // before Sorted
  // showAll: (req, res) => {
  //   Object.find({}, (err, object) => {
  //     if (err) {
  //       res.json(err);
  //     }
  //     else {
  //       res.json(object);
  //     }
  //   })
  // },
  new: (req, res) => {

    Object.findOne({object_name: req.body.object_name}, (err, object) => {
      console.log(object)
        if(err) {
            res.json(err)
        }
      
        if(object) {
            res.json('object already exists')
        }
        else{
        Object.create(req.body, (err) => {
          if(err){
            console.log(err);
              res.json(err);
              // res.redirect('/objects')
          }
          else{
              res.redirect('/objects');
          }
            })
          }
    });    

  },
  show: (req, res) => {
    Object.findOne({_id: req.params.id}, (err, object) => {
      if (err) {
        res.json(err);
      }
      else {
        res.json(object);
      }
    })
  },
  update: (req, res) => {
    Object.findOneAndUpdate({_id: req.params.id}, req.body, (err, object) => {
      if (err) {
        res.json(err);
      }
      else {
        res.json(object);
      }
    })
  },  
  updateOne: (req, res) => {
    Object.findOne({_id: req.params.id}, (err, object) => {

    // let comment = new Comment({text: req.body.text, stars: req.body.stars});
    // comment.cake = cake._id;
    object.likes+= 1;
    object.save((err) => {
      if(err) {
        console.log('Errors saving comment.');
      }
      else {
              res.json(object);
            }
        });
      })
  },
  destroy: (req, res) => {
    Object.remove({_id: req.params.id}, (err) => {
      if (err) {
        console.log("Issue deleting: " + err);
      }
      else {
        res.redirect('/objects');
      }
    })
  }
}

// Room.find({}).sort('-date').exec(function(err, docs) { ... });
// Room.find({}).sort({date: -1}).exec(function(err, docs) { ... });
// Room.find({}).sort({date: 'desc'}).exec(function(err, docs) { ... });
// Room.find({}).sort({date: 'descending'}).exec(function(err, docs) { ... });
// Room.find({}).sort([['date', -1]]).exec(function(err, docs) { ... });
// Room.find({}, null, {sort: '-date'}, function(err, docs) { ... });
// Room.find({}, null, {sort: {date: -1}}, function(err, docs) { ... });


  // new: (req, res) => {
  //   Object.create(req.body, (err) => {
  //       Object.findOne({name: req.body.name}, (err, object) => {
  //               if(object) {
  //                   res.json('object already exists')
  //                 }
  //       });     
  //   if(err){
  //     console.log(err);
  //       res.json(err);
  //       // res.redirect('/objects')
  //   }
  //   else{
  //       res.redirect('/objects');
  //   }
  // })
  // },