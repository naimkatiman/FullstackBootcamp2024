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

$db = $client->myDatabase;
$collection = $db->users;

try {
    // Create Operation
    function createDocument($collection, $document) {
        return $collection->insertOne($document);
    }

    // Read Operation
    function readDocument($collection, $filter = []) {
        return $collection->find($filter);
    }

    // Update Operation
    function updateDocument($collection, $filter, $newData) {
        return $collection->updateOne($filter, ['$set' => $newData]);
    }

    // Delete Operation
    function deleteDocument($collection, $filter) {
        return $collection->deleteOne($filter);
    }

    // Examples of using the CRUD operations
    // Creating a new user
    $insertResult = createDocument($collection, ['name' => 'John Doe', 'email' => 'john@example.com']);
    echo "Inserted document with ID: " . $insertResult->getInsertedId() . "\n";

    // Reading documents
    $users = readDocument($collection);
    foreach ($users as $user) {
        echo $user['_id'], ': ', $user['name'], "\n";
    }

    // Updating a document
    $updateResult = updateDocument($collection, ['name' => 'John Doe'], ['name' => 'John Smith']);
    echo "Updated documents count: " . $updateResult->getModifiedCount() . "\n";

    // Deleting a document
    $deleteResult = deleteDocument($collection, ['name' => 'John Smith']);
    echo "Deleted documents count: " . $deleteResult->getDeletedCount() . "\n";

} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
