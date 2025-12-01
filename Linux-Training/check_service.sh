#!/bin/bash
status=$(jq -r '.status' server.json)
if [ "$status" == "active" ]; then
    echo "Server is active"
else
    echo "Server is under maintenance"
fi