#!/bin/bash
# Displays all methods a server will accept
curl -sI "$1" | grep -i "^Allow" | awk -F ': ' '{print $2'
