let express = require('express'),
     path = require('path'),
     mongoose = require('mongoose'),
     app = express();


const bodyParser = require('body-parser');
app.use(bodyParser.json());
// var Person = require('./server/models/object.js');

app.use(express.static( __dirname + '/myFirstAngularApp/dist/myFirstAngularApp' ));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');


require('./server/config/mongoose.js');
require('./server/config/routes.js')(app);


// app.all('/pets', (req, res, next) => {
//         res.sendFile(path.resolve("./myFirstAngularApp/src/app/object/object.component.html"));
//     });


app.all('*', (req, res, next) => {
        res.sendFile(path.resolve("./myFirstAngularApp/dist/myFirstAngularApp/index.html"));
    });
app.listen(8000, () => {
  console.log(`Listening on port 8000`);
})
