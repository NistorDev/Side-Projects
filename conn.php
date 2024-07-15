<?php
function fetchData() {    //$tableName
    // Database connection parameters
    $hostname = '127.0.0.1:3306';
    $username = 'root';
    $password = 'Drrrk!@!1';
    $database = 'noblesse';

    // Create a MySQL connection
    $conn = new mysqli($hostname, $username, $password, $database);

    // Check the connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Fetch data from the predefined table using a union of 3 tables
    $query = "SELECT * FROM rezervari";          //$tableName
    $result = $conn->query($query);
    // echo $result;
    // Store the fetched data in an array
    $data = array();
    
    echo $result;

    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }

    // Close the database connection
    $conn->close();

    return $data;
}

$rez = fetchData();
echo $rez;

?>