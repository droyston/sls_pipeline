#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:27:38 2020

@author: dylanroyston
"""

import os
import json
from datetime import datetime as dt

fp = '/home/dylanroyston/Documents/GIT/mf_swe_test/samples/person1.json'

with open(fp, "r") as read_file:
    data = json.load(read_file)


# method to extract nested keys
def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

# extract all keys in object
all_keys = []
all_vals = []
for key, value in recursive_items(data):
    all_keys.append(key)
    all_vals.append(value)
    

# search for and extract target key/values, returning 400 if null/missing
target_keys = ['first_name', 'middle_name', 'last_name', 'zip_code']
target_vals = []

for k in target_keys:
    if k in all_keys:
        return_val = all_vals[all_keys.index(k)]
    else:
        return_val = 400
    target_vals.append(return_val)
    
    if None in target_vals:
        repl = target_vals.index(None)
        target_vals[repl] = 400

# append list of all source keys for follow-up
target_keys.append('source_keys')
target_vals.append(all_keys)

# append date of processing for follow-up
currD = str(dt.date(dt.now()))
target_keys.append('load_date')
target_vals.append(currD)

# convert target data to json
extract_dict = dict(zip(target_keys, target_vals))
extract_obj = json.dumps(extract_dict)