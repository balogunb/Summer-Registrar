const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');
var mongoose = require('mongoose');
require('dotenv').config();
const PORT = 4000;

app.use(cors());
app.use(bodyParser.json());

//connect to cluster
//console.log('Insert password');
//var password = prompt("input password");


const server = 'mongodb+srv://'+process.env.DB_USER+':'+process.env.DB_PASSWORD+'@collegecourses-ne1ze.mongodb.net/'+process.env.DB_NAME+'?retryWrites=true&w=majority';
console.log(server);
mongoose.connect(server, {useNewUrlParser: true});
console.log(mongoose.version);
const connection = mongoose.connection;

connection.once('open', function() {
    console.log("MongoDB database connection established successfully");
})

app.listen(PORT, function() {
    console.log("Server is running on Port: " + PORT);
});
