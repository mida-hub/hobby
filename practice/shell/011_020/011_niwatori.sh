#!/bin/bash

var_local="sato"
var_global="shio"

export var_global

sh ./011_tamago.sh

echo " local@niwatori  : ${var_local}"
echo " global@niwatori : ${var_global}"
