#!/bin/bash
echo "start $0"

echo " local@tamago  : ${var_local}"
echo " global@tamago : ${var_global}"

var_local="tamanegi"
var_global="mitsuba"

export var_global

echo "end $0"

