#!/bin/bash
#script to get allowed methods in the server if available through OPTIONS http request
curl -s -I -X OPTIONS "$1" |grep 'Allow:' | cut -f2- -d' '
