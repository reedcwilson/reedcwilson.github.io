
var express = require("express"),
    querystring = require('querystring'),
    request = require('request'),
    router = express.Router(),
    email = process.env.MAIL_EMAIL,
    key = process.env.MAIL_KEY,
    domain = process.env.MAIL_DOMAIN;

router.post('/send', function(req, res) {
  var uri = 'https://api:' + key + '@' + domain + '/messages';
  var data = {
    to: email,
    from: 'postmaster@reedcwilson.com',
    subject: 'Resume Contact Form:' + req.body.name,
    html: '<h3>You received a "contact me" message</h3>' + 
      '<p>Name: ' + req.body.name + '</p>' +
      '<p>Email: ' + req.body.email + '</p>' +
      '<br />' + 
      '<p>' + req.body.message + '</p>'
  }
  var encData = querystring.stringify(data);
  request({
    uri: uri, 
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Length': encData.length
    },
    body: encData, 
    method: 'POST'
  }, function(err, response, body) {
    if (err) {
      //res.render('error', { error : err});
      res.send("HTTP/1.1 INTERNAL ERROR");
      console.log("got an error: ", err);
    }
    else {
      res.send('HTTP/1.1 OK');
    }
  });
});


module.exports = router;
