#!/usr/bin/python3
"""Sends a REQUEST to a url and displays the body of the response
and handles the error status"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
