#!/usr/bin/python3
"""
This script adds command-line arguments to a JSON file and saves the data
"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

data = list(load_from_json_file(filename))

for i in range(1, sys.argv):
    data.append(sys.argv[i])

save_to_json_file(data, filename)
