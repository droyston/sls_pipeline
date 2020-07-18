#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:16:46 2020

@author: dylanroyston
"""

import os
import boto3


def handler(event, context):
    """
    trigger the glue crawler that creates a data catalog
    from the extracted contents of the jsons.
    """
    # get glue crawler name from the environment
    glue_crawler = os.getenv('GLUE_CRAWLER')

    # get the state of the glue crawler and start if it's ready,
    # else do nothing.
    glue_client = boto3.client('glue')
    crawler_metadata = glue_client.get_crawler(Name=glue_crawler)
    crawler_state = crawler_metadata.get('Crawler').get('State')
    
    if crawler_state == 'READY':
        print('crawler is ready, so we are starting it ...')
        result = glue_client.start_crawler(Name=glue_crawler)
        print('crawler result {}'.format(result))
    
    print('crawler is in state {}. only start '
          'crawler when in state READY'.format(crawler_state))
    return crawler_state
