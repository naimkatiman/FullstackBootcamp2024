var express = require('express');
var app = express();

var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

// Use the service name 'db' to connect to MongoDB
var url = 'mongodb://db:27017';

MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected correctly to server.");
  const db = client.db('test'); // Use 'test' or any other database name you prefer

  // Define the route inside the MongoDB connection callback
  app.get('/', function (req, res) {
    res.send('Hello World!');
  });

  // No need to close the db connection here
});

// Start the server regardless of the database connection
app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
