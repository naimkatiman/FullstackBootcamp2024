<?php
$temperature = 17;

if ($temperature < 0) {
    echo "Very cold";
} else if ($temperature >= 0 && $temperature < 15) {
    echo "cold";
} else if ($temperature >= 15 && $temperature < 30) {
    echo "Not too bad";
} else {
    echo "Too hot";
}
