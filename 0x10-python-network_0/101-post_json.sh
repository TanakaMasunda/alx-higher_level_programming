#!/bin/bash
# scrpt send JSON POST rqst 2 URL as 1st arg & dsplay body of response,POST rqst wth content of file,wth filename as 2nd arg of rqst,use curl
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
