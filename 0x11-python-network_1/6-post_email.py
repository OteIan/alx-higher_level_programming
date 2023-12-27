#!/usr/bin/python3
"""Sends a POST request then displays the body of the url"""
import sys
import requests


if __name__ == "__main__":
    url, email = sys.argv[1:]
    data = {'email': email}

    print(requests.post(url, data=data).text)
