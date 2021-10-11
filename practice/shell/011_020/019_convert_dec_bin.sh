#!/bin/bash

# 2->10
bin=1000001
dec=`echo "ibase=2; $bin" | bc`
echo $dec

# 10->2
dec=65
bin=`echo "obase=2; $dec" | bc`
echo $bin
