#!/bin/bash

number_string=""
echo $number_string

# 10進数で数値チェック
if [ -z "`echo "$number_string" | grep '^[0-9]\+$'`" ]; then
    echo "Invalid number!"
    exit 1
fi

# 16進数で数値チェック
if [ -z "`echo "$number_string" | grep '^0x[0-9A-Fa-f]\+$'`" ]; then
    echo "Invalid number!"
    exit 1
fi

# 8進数で数値チェック
if [ -z "`echo "$number_string" | grep '^0[0-7]*$'`" ]; then
    echo "Invalid number!"
    exit 1
fi

# 2進数で数値チェック
if [ -z "`echo "$number_string" | grep '^[01]\+$'`" ]; then
    echo "Invalid number!"
    exit 1
fi
