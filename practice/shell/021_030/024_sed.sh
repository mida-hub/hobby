#!/bin/bash

sql_string="SELECT * FROM table_1"
pattern="FROM"
replace="from"

echo "${sql_string}"
match_str=`echo "${sql_string}" | sed "s/${pattern}/${replace}/g"`
echo "${match_str}"
