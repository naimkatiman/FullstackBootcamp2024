<?php
// Declare variables
$servername = "localhost";
$username = "naim";
$password = "Naim123";
$database = "newdb";
$port = 1111; // Specify the port number MySQL is listening on

// Create a connection
$conn = new mysqli($servername, $username, $password, $database, $port);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected Successfully";
?>
