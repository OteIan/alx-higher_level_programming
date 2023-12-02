#!/bin/bash
# Displays all methods a server will accept
curl -siX OPTIONS "$1"
