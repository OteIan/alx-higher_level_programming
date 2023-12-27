#!/usr/bin/python3
"""Sends a POST request with JSON formatting"""
import sys
import requests


def search_api(url, letter):
    """Sends a POST request"""
    params = {'q': letter}

    response = requests.post(url, data=params)
    try:
        data = response.json()
        if data == {}:
            print('No result')
        else:
            print(f"[{data.get('id')}] {data.get('name')}")

    except ValueError:
        print('Not a valid JSON')


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'

    search_api(url, letter)
