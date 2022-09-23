#!/bin/bash
# script tht make rqst 2 0.0.0.0:5000/catch_me tht cz server 2 respond wth msg"You got me!", in body of response,use curl,not echo, cat, etc.
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
