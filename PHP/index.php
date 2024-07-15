<!DOCTYPE html>
<html>
    <head>
        <title>Age Category Checker</title>
    </head>
<body>
    <h2>Age Category Checker</h2>
    <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
    Enter your age: <input type="text" name="age">
    <input type="submit" value="submit">
</form>

<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get input from user
    $age = $_POST["age"];

    // Check the age category
    if($age < 13) {
        echo "You are a child";
    } else if($age >= 13 && $age < 20) {
        echo "You're a teenager";
    }else{
        echo "You're an adult";
    }    
}
?>
</body>
</html>
