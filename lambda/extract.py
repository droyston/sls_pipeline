#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:16:46 2020

@author: dylanroyston
"""


import json
import os
from datetime import datetime as dt

import boto3


def handler(event, context):
    """
    extract the contents from the jsons and
    put the resulting object back to s3.
    """
    # get the source key and bucket from
    # the event that triggered this lambda function.
    source_key = event['Records'][0]['s3']['object']['key']
    source_bucket = event['Records'][0]['s3']['bucket']['name']

    # get the destination key and bucket 
    # from the environment variables
    destination_bucket = os.getenv('DEST_BUCKET')
    destination_key = os.getenv('DEST_KEY')

    # get the json name from the key
    source_name = source_key.split('/')[-1]

    # get json from s3, extract the contents
    # and dump the result back to s3
    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(Bucket=source_bucket,
                                     Key=source_key)["Body"].read().decode('utf-8')
    
    source_raw = json.loads(s3_object)

    # retrieve target data from source
    source_object = extract_contents(source_raw, source_name)
    
    procD = source_object['load_date']
    source_out = json.dumps(source_object)
    full_s3_key = destination_key + source_name + '_' + str(procD) + '_extract.json'
    
    s3_client.put_object(Body=source_out,
                         Bucket=destination_bucket,
                         Key=full_s3_key)


## secondary functions

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)
        

def extract_contents(message_object, obj_name):
        
    message_data = json.loads(message_object)

    # extract all keys in object
    all_keys = ['id']
    all_vals = [obj_name]
    
    for key, value in recursive_items(message_data):
        all_keys.append(key)
        all_vals.append(value)
        
    # search for and extract target key/values, returning 400 if null/missing
    target_keys = ['first_name', 'middle_name', 'last_name', 'zip_code']
    target_vals = []
    
    for k in target_keys:
        if k in all_keys:
            return_val = all_vals[all_keys.index(k)]
        else:
            return_val = '400'
        target_vals.append(return_val)
        
        if None in target_vals:
            repl = target_vals.index(None)
            target_vals[repl] = '400'
    
    # append list of all source keys for follow-up
    target_keys.append('source_keys')
    target_vals.append(all_keys)
    
    # append date of processing for follow-up
    currD = str(dt.date(dt.now()))
    target_keys.append('load_date')
    target_vals.append(currD)
    
    # convert target data to json
    extract_dict = dict(zip(target_keys, target_vals))


    return extract_dict



