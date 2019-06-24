const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');
const PORT = 4000;

app.use(cors());
app.use(bodyParser.json());

//connect to cluster
//console.log('Insert password');
//var password = prompt("input password");

mongoose.connect('mongodb+srv://Basitb:Adebowale2010@collegecourses-ne1ze.mongodb.net/test?retryWrites=true&w=majority')

const connection = mongoose.connection;

connection.once('open', function() {
    console.log("MongoDB database connection established successfully");
})

app.listen(PORT, function() {
    console.log("Server is running on Port: " + PORT);
});
