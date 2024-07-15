<?php
require 'vendor/autoload.php'; 

function getConnection() {
    $client = new MongoDB\Client("mongodb://localhost:27017");
    return $client->selectDatabase('newdb');
}

function insertUser($username, $email, $age) {
    $db = getConnection();
    $collection = $db->users;
    try {
        $result = $collection->insertOne([
            'username' => $username,
            'email' => $email,
            'age' => $age
        ]);
        echo "Inserted with Object ID '{$result->getInsertedId()}'\n";
    } catch (Exception $e) {
        echo "Insert failed: " . $e->getMessage() . "\n";
    }
}

function findAllUsers() {
    $db = getConnection();
    $collection = $db->users;
    try {
        $cursor = $collection->find();
        foreach ($cursor as $document) {
            echo "Username: " . $document['username'] . ", Email: " . $document['email'] . "\n";
        }
    } catch (Exception $e) {
        echo "Find failed: " . $e->getMessage() . "\n";
    }
}

function updateUserAge($username, $newAge) {
    $db = getConnection();
    $collection = $db->users;
    try {
        $result = $collection->updateOne(
            ['username' => $username],
            ['$set' => ['age' => $newAge]]
        );
        echo "Matched {$result->getMatchedCount()} and modified {$result->getModifiedCount()} documents\n";
    } catch (Exception $e) {
        echo "Update failed: " . $e->getMessage() . "\n";
    }
}

function deleteUser($username) {
    $db = getConnection();
    $collection = $db->users;
    try {
        $result = $collection->deleteOne(['username' => $username]);
        echo "Deleted {$result->getDeletedCount()} document(s)\n";
    } catch (Exception $e) {
        echo "Delete failed: " . $e->getMessage() . "\n";
    }
}

// Test the functions
insertUser('naim', 'naim123@gmail.com', 25);
findAllUsers();
updateUserAge('naim', 26);
deleteUser('naim');
?>
