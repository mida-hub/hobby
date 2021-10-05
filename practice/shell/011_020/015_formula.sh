#!/bin/bash

a=7
b=-56
c=105

formula1="(-($b) + sqrt(($b)^2 -4*($a)*($c)) ) / (2*($a))"
formula2="(-($b) - sqrt(($b)^2 -4*($a)*($c)) ) / (2*($a))"

solution1=`awk "BEGIN{print $formula1}"`
solution2=`awk "BEGIN{print $formula2}"`

echo "The answers are "$solution1" and "$solution2"."
