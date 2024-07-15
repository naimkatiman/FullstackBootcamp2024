<?php
for ($i = 0; $i < 6; $i++) {
    echo "The number is: $i" . "\n";
}

$j = 1;
while ($j <= 5) {
    echo "The number is $j" . "\n";
    $j++;
}
while ($j <= 10);


for ($i = 1; $i <= 3; $i++) {
    for( $j = 1; $j <= 3; $j++) {
        echo "($i, $j)" . "\n";
    }
}
