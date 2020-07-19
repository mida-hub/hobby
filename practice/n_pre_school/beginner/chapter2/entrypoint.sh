#!/bin/bash
/etc/init.d/cron restart
cd /work/httpd
/usr/bin/python3.8 -m http.server 8000