#!/bin/sh

start_num=10
end_num=30

to_val=`expr $end_num - $start_num + 1`
# echo $to_val
for i in `yes "" | cat -n | head -$end_num | tail -$to_val`; do
    echo $i
done
