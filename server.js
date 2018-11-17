
var express = require('express');
var app = express();

var port = process.env.PORT || 3000;
var cp=""

app.use(express.static('public'));


app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.get('/api', function (req, res) {
  res.send('Hello World!');
});

app.get('/setpice1', function (req, res) {
  cp="1"
  res.end(cp)
});

app.get('/setpice2', function (req, res) {
  cp="2"
  res.end(cp)
});

app.get('/board', function (req, res) {
  res.end(cp)
});

app.get('/clear', function (req, res) {
  cp=""
  res.end(cp)
});

app.listen(port, function () {
  console.log('Example app listening on port 3000!');
});
