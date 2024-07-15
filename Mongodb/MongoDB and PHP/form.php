<?php
$username = $_POST['username'];
$password = $_POST['password'];

$connectionString = "mongodb://$username:$password@localhost:27017";

// Create the MongoDB Client
try {
    $client = new MongoDB\Client($connectionString);
} catch (Exception $e) {
    die("Error connection to MongoDB: " . $e->getMessage());
}

// Select a database
$database = $client->phpdb;
// Select a collection
$collection = $database->phpform;

// Process form submission
if ($_SERVER['REQUEST_METHOD'] == "POST") {
    // Insert a document
    try {
        $insertResult = $collection->insertOne([
            'name' => $_POST['name'],
            'email' => $_POST['email'],
            'message' => $_POST['message']
        ]);
        echo "Document inserted successfully";
    } catch (Exception $e) {
        echo "Error inserting document: " . $e->getMessage();
    }
}
?>
