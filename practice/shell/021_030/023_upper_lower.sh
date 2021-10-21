#!/bin/bash

character1="Capital"
character2="Small"

echo ${character1}
character1=`echo "${character1}" | tr "a-z" "A-Z"`
echo ${character1}

echo ${character2}
character2=`echo "${character2}" | tr  "A-Z" "a-z"`
echo ${character2}
