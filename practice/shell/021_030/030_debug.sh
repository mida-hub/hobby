#!/bin/bash

cat sample.txt | tee /dev/stderr | wc -l
