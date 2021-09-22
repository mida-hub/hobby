#!/bin/bash

cat /not_exist_file.txt > /dev/null
if [ $? -ne 0 ]; then
    echo "*** error"
fi

cat /not_exist_file.txt > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "*** error"
fi
