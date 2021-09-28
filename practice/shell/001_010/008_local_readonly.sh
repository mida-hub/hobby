#!/bin/bash

f_soba() {
    local yakumi
    yakumi="wasabi"
    echo $yakumi
}

yakumi="negi"
echo $yakumi
f_soba
echo $yakumi

gohan=58
readonly gohan
