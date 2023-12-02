#!/bin/bash
# Displays all methods a server will accept
curl -iX OPTIONS -s "$1" | grep -i Allow | awk '{print $2}'
