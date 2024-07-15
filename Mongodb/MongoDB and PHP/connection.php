<?php
require 'vendor/autoload.php';  // Autoloader for composer

use MongoDB\Client;
use MongoDB\Driver\ServerApi;

// Set URI
$uri = 'mongodb://localhost:27017';

// Create a new ServerApi object
$serverApi = new ServerApi(ServerApi::V1);

// Create client and connect to server
$client = new Client($uri, [], ['serverApi' => $serverApi]);

try {
    // Send a command to the database
    $result = $client->selectDatabase('admin')->command(['ping' => 1]);
    echo "Connection successful: ";
    print_r($result->toArray());
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
