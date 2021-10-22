#!/bin/bash

file_path="/food/nihon/yoshoku/hayashirice.txt"
file_name="${file_path##*/}"
dir_name="${file_path%/*}"

echo ${file_path}
echo ${file_name}
echo ${dir_name}
