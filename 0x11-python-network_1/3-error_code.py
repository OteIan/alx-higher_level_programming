#!/usr/bin/python3
"""Sends a REQUEST to a url and displays the body of the response
and handles the error status"""
from urllib import request, error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf8'))
    except error.HTTPError as e:
        print(f"Error code: {e}")