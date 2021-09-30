#!/bin/bash

global1="sato"
global2="shio"

export global1
export global2

temp_file=`mktemp /tmp/ONABE_GUTSUGUTSU.XXXXX`
export temp_file

sh ./012_tamago.sh

for variable in `cat ${temp_file}`; do
    # echo ${variable}
    eval ${variable}
done

rm -f $temp_file

echo " global1@niwatori : ${global1}"
echo " global2@niwatori : ${global2}"
