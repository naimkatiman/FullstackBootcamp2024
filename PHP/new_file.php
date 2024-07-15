<?

// One line comment
/*
Multi line comment
Another comment
*/

?>

<?php // variables
$text = "Hello, World!";
$number = 10;
?>

<?/*Strings: Textual data
    Integers: Whole numbers
    Floats (or doubles): Numbers with a decimal point
    Booleans: True or false values
    Arrays: Collections of data
    Objects: Instances of classes
    NULL: Represents a variable with no value */?>

<?php
$string = "This is a string";
$integer = 100;
$float = 10.5;
$boolean = true;
$array = array("apple", "banana", "cherry");
?>
    
<?php //string
$single_quoted = 'This is a single-quoted string.';
$double_quoted = "This is a double-quoted string.";
?>

<?php
// Indexed array
$colors = array("Red", "Green", "Blue");

// Associative array
$age = array("Peter" => "35", "Ben" => "37", "Joe" => "43");

// Multidimensional array
$cars = array (
  array("Volvo",22,18),
  array("BMW",15,13),
  array("Saab",5,2),
  array("Land Rover",17,15)
);
?>

<?php
// If-else statement
if ($a > $b) {
  echo "a is greater than b";
} else {
  echo "a is not greater than b";
}

// While loop
while ($i <= 10) {
  echo $i++;
}

// For loop
for ($i = 1; $i <= 10; $i++) {
  echo $i;
}
?>

$hasPermission = True;