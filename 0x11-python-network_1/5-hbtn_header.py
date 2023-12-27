#!/usr/bin/python3
"""Fetches the status of a given url"""
import requests
import sys


if __name__ == "__main__":
    content = requests.get(sys.argv[1])

    print(content.headers.get('X-Request-Id'))
