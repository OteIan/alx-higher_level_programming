#!/usr/bin/python3
"""Fetches the status of a given url"""
import requests


if __name__ == "__main__":
    content = requests.get("https://alx-intranet.hbtn.io/status").text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
