#!/bin/bash

# 16->10
hex=0x10
dec=`printf "%d" $hex`
echo $dec

# 8->10
oct=010
dec=`printf "%d" $oct`
echo $dec

# 10->16
dec=16
hex=`printf "0x%x" $dec`
echo $hex

# 10->8
dec=8
oct=`printf "0%o" $dec`
echo $oct
