#!/usr/bin/python3
"""Request header from a url"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header_info = response.headers.get("X-Request-Id")
    print(header_info)
