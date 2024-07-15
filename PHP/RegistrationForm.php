<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
</head>

<body>
    <h2>Registration Form</h2>
    <form method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>

        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age" required><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required minlength="8"><br>

        <input type="submit" value="Register">
    </form>

    <?php

    $errors = [];

    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        if (empty($_POST["name"])) {
            $errors[] = "Name is required.";
        } else if (!preg_match("/^[a-zA-Z ]*$/", $_POST["name"])) {
            $errors[] = "Name must be alphabetic characters only.";
        }

        if (empty($_POST["email"])) {
            $errors[] = "Email is required.";
        } else if (!filter_var($_POST["email"])) {
            $errors[] = "Invalid email format.";
        }


        if (empty($_POST["age"])) {
            $errors[] = "Age is required.";
        } else if (!filter_var($_POST["age"])) {
            $errors[] = "Age must be a number between 18 and 65.";
        }


        if (empty($_POST["password"])) {
            $errors[] = "Password is required.";
        } else if (strlen($_POST["password"]) < 8) {
            $errors[] = "Password must be at least 8 characters long.";
        }


        if (!empty($errors)) {
            foreach ($errors as $error) {
                echo "<p>$error</p>";
            }
        } else {
            echo "<p>Thank you for the Registration!</p>";
        }
    }
    ?>

</body>

</html>