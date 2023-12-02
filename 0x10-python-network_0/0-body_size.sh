#!/bin/bash
# Displays the size of the body of a URL in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
