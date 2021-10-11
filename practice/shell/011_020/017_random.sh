#!/bin/bash

random_value=`awk "BEGIN{srand(); print int(6 * rand() + 1)}"`

echo "The answer is \"$random_value\"."
