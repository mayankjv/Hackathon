var express = require("express");
var app = express();
var bodyParser = require("body-parser");
app.use(express.static('views'));





app.get("/", function(req, res){


	res.render("index.ejs");
});


var port = 8080;
app.listen(port, () => {
	console.log("we are live on " + port);
});