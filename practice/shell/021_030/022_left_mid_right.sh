#!/bin/bash

string="12345678901234567890"
left_word=`echo "$string" | cut -c -8`
echo $left_word

mid_word=`echo "$string" | cut -c 9-13`
echo $mid_word

right_word=`echo "$string" | cut -c $(expr ${#string} + 1 - 7)-`
echo $right_word
