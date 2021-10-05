#!/bin/bash

hnCalorie=" "

eval hnCalorie_zarusoba=\"300\" ; hnCalorie="${hnCalorie}zarusoba "
eval hnCalorie_doria=\"700\" ; hnCalorie="${hnCalorie}doria "
eval hnCalorie_unadon=\"650\" ; hnCalorie="${hnCalorie}unadon "

echo ${hnCalorie}

for key in ${hnCalorie}; do
    # echo "${key}"
    eval echo "${key} : \$hnCalorie_$key"
done
