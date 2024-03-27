#!/bin/bash
#shellcheck disable=SC2046
if [$(curl -l -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -ls "$1";
