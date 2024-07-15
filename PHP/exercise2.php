<?php
$age = 25;

if ($age < 13) {
    $category = "Child";
} elseif ($age >= 13 && $age <= 19) {
    $category = "Teenager";
} else {
    $category = "Adult";
}
echo "Hi " . $category . ".";

