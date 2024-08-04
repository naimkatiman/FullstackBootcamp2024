<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$servername = "localhost";
$username = "root";
$password = "57752369";
$database = "student_data";

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if (empty($_POST['first_name']) || empty($_POST['last_name']) || empty($_POST['email']) || empty($_POST['address']) || empty($_POST['password'])) {
    echo "All fields are required";
    exit;
}

$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];
$email = $_POST['email'];
$address = $_POST['address'];
$password = $_POST['password'];

// Validation and sanitization (not included in this example)

$sql = "CREATE TABLE IF NOT EXISTS Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    password VARCHAR(255) NOT NULL
)";
$conn->query($sql);

$sql = "INSERT INTO users (first_name, last_name, email, address, password) VALUES (?, ?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("sssss", $first_name, $last_name, $email, $address, $password);
$stmt->execute();

if ($stmt->execute()) {
    echo "Data inserted successfully.";
} else {
    echo "Error: " . $conn->error;
}


if ($stmt->affected_rows > 0) {
    echo "Registration successful";
} else {
    echo "Error registering user";
}

$stmt->close();
$conn->close();
