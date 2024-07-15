<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
   
    require 'vendor/autoload.php';

    $client = new MongoDB\Client("mongodb://localhost:27017");

    $db = $client->student_records;
    $collection = $db->students;

    // Get data from form
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $age = (int) $_POST['age'];
    $course = htmlspecialchars($_POST['course']);

    // Insert data into the collection
    $insertOneResult = $collection->insertOne([
        'name' => $name,
        'email' => $email,
        'age' => $age,
        'course' => $course
    ]);

    // Check if the insert was successful
    if ($insertOneResult->getInsertedCount() == 1) {
        echo "Record added successfully.";
    } else {
        echo "Error adding record.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Student Registration</title>
</head>
<body>
    <h1>Register Student</h1>
    <form method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label><br>
        <input type="text" id="email" name="email" required><br><br>
        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age" required min="10"><br><br>
        <label for="course">Course:</label><br>
        <input type="text" id="course" name="course" required><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
