# mf_swe_test
Takehome interview assignment

## Table of Contents
1. [Overview](#about)
2. [Engineering Design](#engineering-design)
3. [Deployment](#deployment)
4. [Credits](#credits)
5. [Reference](#references)


## Overview

Challenge: Deploy a serverless data pipeline to ingest and store JSON data in AWS

## Engineering Design

### Pipeline

This pipeline was built using the following AWS tools:
 - API Gateway: present an endpoint for user submission of JSON data
 - S3: store raw (source) and extracted JSON files
 - Lambda: execute ETL functions in Python to extract and store target fields
 - Glue: crawl over extracted JSON files to enable querying
 - Athena: query extracted JSON file content

Data flow:
 - User submits JSON structure to API endpoint via Postman
 - "Upload.py" takes in body and writes a JSON object to S3
 - "Extract.py" recursively searches for target fields and writes a new JSON object to S3
 - "Load.py" triggers a Glue crawler to assess extracted JSONs and creates Athena table
 - Athena presents extracted data for querying
 
 
### Design choices
 - Raw source data is stored in original JSON for follow-up analysis
 - Extracted JSONs contain target data (first_name, middle_name, last_name, zip_code), as well as all unused source fields for more rapid follow-up
	- Missing or null target data returns '400'
 - Processing date is appended to extracted filename for timeseries Athena partitioning

## Deployment

Pipeline is deployed using ([Serverless)(https://www.serverless.com/)) framework
'''
npm install -g serverless
'''

Requires appropriately permissioned AWS roles, which need to be inserted into 'serverless.yml' in the ROLE and GLUE-ROLE fields

deploy with 
'''
sls deploy --stage <UNIQUE-IDENT>
'''

Send PUT commands with ([Postman](https://www.postman.com/))


## Credits

This project was developed by Dylan Royston ([LinkedIn Profile](https://www.linkedin.com/in/dylanroyston/)) as a take-home technical challenge for ([Manifold.AI](https://www.manifold.ai/manifold))

## References

inspired by ([this](https://towardsdatascience.com/build-a-serverless-data-pipeline-on-aws-7c7d498d9707)) Towards Data Science article




