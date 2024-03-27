#!/bin/bash
#script to send delete request to the url passed and displays response
curl -s -X DELETE "$1"
