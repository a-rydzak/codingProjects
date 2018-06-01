const object= require('../controllers/object.js');


module.exports = (app) => {
  app.get('/objects', (req, res) => {

    object.showAll(req, res);
  })
  app.post('/objects', (req, res) => {
    object.new(req, res);
  })
  app.get('/objects/:id', (req, res) => {
    object.show(req, res);
  })
  app.put('/objects/:id', (req, res) => {
    object.update(req, res);
  })
  app.put('/objectss/:id', (req, res) => {
    object.updateOne(req, res);
  })
  app.delete('/objects/:id', (req, res) => {
    object.destroy(req, res);
  })
}
