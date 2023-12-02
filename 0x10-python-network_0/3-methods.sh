#!/bin/bash
# Displays all methods a server will accept
curl -sX OPTIONS "$1"
