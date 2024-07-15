//import  createConnection from 'mysql'; 



// import mysql from 'mysql';


var express    = require("express");

const mysql = require('mysql');


const connection  = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : 'Drrrk!@!1',
    database : 'noblesse'
});

connection.connect((err) => {
  if(err) throw err;
  console.log('Connected to MySQL Server!');
});


