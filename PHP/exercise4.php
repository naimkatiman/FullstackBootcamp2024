<!DOCTYPE html>
<html>
<head>
    <title>Rectangle Area Calculator</title>
</head>
<body>
    <h1>Rectangle Area Calculator</h1>
    <form method="post">
        <h2>Rectangle 1</h2>
        Width: <input type="number" name="width1" required>
        Height: <input type="number" name="height1" required><br>

        <h2>Rectangle 2</h2>
        Width: <input type="number" name="width2" required>
        Height: <input type="number" name="height2" required><br>

        <input type="submit" value="Calculate Areas">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $width1 = $_POST['width1'];
        $height1 = $_POST['height1'];
        $area1 = $width1 * $height1;

        $width2 = $_POST['width2'];
        $height2 = $_POST['height2'];
        $area2 = $width2 * $height2;

        echo "<p>Rectangle 1 is: $area1 square units.</p>";
        echo "<p>Rectangle 2 is: $area2 square units.</p>";
    }
    ?>
</body>
</html>
