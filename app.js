
var express = require('express'),
    app = express(),
    bodyParser = require('body-parser');

var path = require('path'),
    mail = require('./mail');

app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, 'public/index.html'));
});


app.use('/mail', mail);


app.set('port', process.env.PORT || 3000);

var server = app.listen(app.get('port'), function () {
  console.log('Resume listening at http://%s:%s', server.address().address, app.get('port'));
});
