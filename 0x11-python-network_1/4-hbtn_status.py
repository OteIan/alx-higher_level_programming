#!/usr/bin/python3
"""Fetches the status of a given url"""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        content = response.read().decode('utf-8')
    
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")