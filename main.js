

// const x1  = document.forms["infocli"];
// let numClic = document.getElementById("txt1");
// let prenClic = document.getElementById("txt2");
// let receptClic = document.getElementById("selectr");
// let tipcc = document.getElementById("selectc");




//  let x =  document.getElementsByTagName('button').onclick = function() {  
//       console.log(numCli, prenCli);
//     };  
  //console.log(numCli, prenCli,tipc);
  // function savcl() {
  //   console.log(numCli, prenCli);
  // }


//import createPool from 'mysql';

// // var connection = createConnection({




// pool.getConnection(function(err, connection) {
//     // Use the connection
//     connection.query( 'SELECT * FROM camere', function(err, rows) {
//         // And done with the connection.
//         connection.release();
//         console.log(rows)
//         // Don't use the connection here, it has been returned to the pool.
//     });
// });

// // The pool will emit a connection event when a new connection is made within the pool.
// // If you need to set session variables on the connection before it gets used, you can listen to the connection event.
// pool.on('connection', function (connection) {
//     console.log("Connected");
//     // Set a session variable
//     //connection.query('SET SESSION auto_increment_increment=1')
// });

// // <<< CLOSE THE CONNECTION USING pool.end >>>
// // When you are done using the pool, you have to end all the connections or the Node.js 
// // event loop will stay active until the connections are closed by the MySQL server. 
// // This is typically done if the pool is used in a script or when trying to gracefully shutdown a server.
// // To end all the connections in the pool, use the end method on the pool:

// pool.end(function (err) {
//     // all connections in the pool have ended
// });

// // connection.connect();

// // connection.connect(function(err) {
// //     // in case of error
// //     if(err){
// //         console.log(err.code);
// //         console.log(err.fatal);
// //     }
// // });

// // $query = 'SELECT * from camere LIMIT 10';

// // connection.query($query, function(err, rows, fields) {
// //     if(err){
// //         console.log("An error ocurred performing the query.");
// //         return;
// //     }

// //     console.log("Query succesfully executed: ", rows);
// // });

// // // Close the connection
// // connection.end(function(){
// //     // The connection has been closed
// // });

// document.addEventListener('DOMContentLoaded', () => {
//   const form = document.querySelector('form');
  // const iframe = document.getElementById('search-iframe');

  // form.addEventListener('submit', async (e) => {
  //   e.preventDefault();
  //   // result.textContent = 'Searching...';

  //   const word = e.target.elements.txt1.value;
  //   console.log(word);
  //   // const response = await fetch('/search', {
  //   //   method: 'POST',
  //   //   body: new URLSearchParams({ word }),
  //   //   headers: {
  //   //     'Content-Type': 'application/x-www-form-urlencoded',
  //   //   },
  //   // });

  // //   if (response.ok) {
  // //     const data = await response.text();
  // //     iframe.contentDocument.body.innerHTML = 'Definition: ' + data;
  // // } else {
  // //     iframe.contentDocument.body.innerHTML = 'An error occurred.';
  // //   }
  // });

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');

  form.addEventListener('submit', async (val)=> {
    val.preventDefault();

  const numCli= val.target.txt1.value;
  const prenCli = val.target.txt2.value;
  const receptCli = val.target.selectr.value;
  const tipc = val.target.selectc.value;

  console.log(tipcc.value);
  console.log(numCli, prenCli, receptCli, tipc);

  tipcc.value = "Tip camera";
});


});
