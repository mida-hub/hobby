#!/bin/bash

undef="NO"
# character="test"
# echo "${character-UNDEF}"

# character 変数が未定義の場合、1つ目のifがTRUEになる
if [ "${character-UNDEF}" = "UNDEF" ]; then
    if [ "${character}" = "" ]; then
        undef="YES"
    fi
fi

echo ${undef}
