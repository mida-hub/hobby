#!/bin/bash

stat -x ./sample.txt | awk "/Modify:/{print \$2,\$3,\$4,\$5,\$6}"
