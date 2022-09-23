#!/bin/bash
# script take in URL, send request to URL & display size of body of the response
curl -s "$1" | wc -c
