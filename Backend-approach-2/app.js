var express = require("express");
var app = express();
var bodyParser = require("body-parser");
var graph = require('fbgraph');
var FB = require('fb');
var likes;


app.use(express.static('views'));
var access_token = 'EAACEdEose0cBAO5gCjASHZCUMw3MUaUqGi9eokdQIOj3x6V4BkCFltYibkCdgFjYFJZBx1KgNz87Jhpfiq3HTZAr3ZBKftVNgLTBQfHGaNqnOMPJjQ9loHuaTz5QuGKEkcZBQcaOpaXUFVTMRZAAfAsEkiaftGdBNeuEm3jcrkHFQZA88bdfPr9BjM86GDAZACWfD4UJIXoB6gZDZD';
FB.setAccessToken(access_token);



FB.api(
  '/me',
  'GET',
  {"fields":"id,name,likes"},
  function(response) {
      likes = response.likes;
  }
);



var port = 8080;
app.listen(port, () => {
	console.log("we are live on " + port);
});
