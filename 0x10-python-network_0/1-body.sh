#!/bin/bash
# script that takes in a URL, sends a GET request to the URL & display the body(200 status code) response
curl -sL "$1"
