#!/bin//bash
#script that gets body size of request
curl -ls "$" | grep -w 'Content-Length' | cut -f2 -d' '
