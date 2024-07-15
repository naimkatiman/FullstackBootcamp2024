<?php
// Define the function to take 2 arguments
function add($a, $b)
{
    return $a + $b;
}

// Call the function with arguments
$result = add(3, 5);
echo "The result is $result" . "\n";

function displayMessage($message)
{
    echo "" . $message . "";
}
//call the function
displayMessage("Hello");

$globalVar = "This is a global variable";

function myFunction()
{
    global $globalVar;
    echo $globalVar;
}

myFunction();

function increment()
{
    static $count = 0;
    $count++;
    echo $count . "\n";
}

increment();
increment();
increment();