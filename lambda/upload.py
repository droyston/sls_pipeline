#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:16:46 2020

@author: dylanroyston
"""

import os
import json
import boto3
import string
import random


def handler(event, context):


    destination_bucket = os.getenv('DEST_BUCKET')
    destination_key = os.getenv('DEST_KEY')
    
    n=16
    rid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    
    event_body = event['body']
    
    event_obj = json.dumps(event_body)

    full_s3_key = destination_key + rid + '.json'

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(destination_bucket)
    bucket.put_object(
        ACL='bucket-owner-full-control',
        ContentType='application/json',
        Key=full_s3_key,
        Body=event_obj
    )

    # validation output
    body = {
        "uploaded": "true",
        "bucket": destination_bucket,
        "path": full_s3_key,
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
