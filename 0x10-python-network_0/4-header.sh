#!/bin/bash
# script take URL as argument,send GET request 2 URL & display body of the response,A header variable X-School-User-Id must be sent with the value 98
curl -sH "X-School-User-Id: 98" "${1}"
