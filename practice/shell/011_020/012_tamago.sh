#!/bin/bash
echo "start $0"

echo " global1@tamago : ${global1}"
echo " global2@tamago : ${global2}"

global1="tamanegi"
global2="mitsuba"

if [ -f "${temp_file}" ]; then
    for variable in global1 global2; do
        # echo "${variable}=\'\$$variable\'"
        eval echo "${variable}=\'\$$variable\'" >> ${temp_file}
    done
fi

echo "end $0"
