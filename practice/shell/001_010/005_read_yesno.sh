#!/bin/bash

check=""
while [ -z "$check" ]; do
    echo -n "Do you like Miso soup (Y/N) ? "
    
    read check

    case $check in
        [Yy]*)
            check="YES"
            ;;
        [Nn]*)
            check="NO"
            ;;
        *)
            echo '*** Answer with "Yes" or "No" !'
            check=""
            ;;
    esac
done
