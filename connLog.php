<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve user input
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Replace this with your actual authentication logic
    // For example, you might check against a database of user credentials
    $validUsername = "demo";
    $validPassword = "password123";

    // Check if input matches valid credentials
    if ($username == $validUsername && $password == $validPassword) {
        echo "Login successful!";
    } else {
        echo "Invalid username or password. Please try again.";
    }
}
?>
