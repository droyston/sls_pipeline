# mf_swe_test
Takehome interview assignment



## Table of Contents
1. [Overview](#about)
2. [Engineering Design](#engineering-design)
3. [Deployment](#deployment)
4. [Credits](#credits)
5. [Reference](#references)





## Overview



## Engineering Design

### Processing Pipeline


Core Dependencies

Anaconda (Python3.7)
- numpy: numerical and linear algebra operations
- pandas: intermediate dataframes
- psycopg2: psql interaction
- boto3: AWS S3 interaction
- Dash (plotly): web API

### Processing Logic


### Data Source


## Deployment


serverless data pipeline demployment demo

sourced from https://towardsdatascience.com/build-a-serverless-data-pipeline-on-aws-7c7d498d9707


requires serverless and appropriately permissioned AWS roles

these roles must be inserted into 'serverless.yml' in the ROLE and GLUE-ROLE fields

deploy with 
| sls deploy --stage <UNIQUE-IDENT>

copy glue scripts into s3 with
| aws s3 cp glue/ s3://serverless-data-pipeline-<UNIQUE-IDENT>-glue-scripts/ --recursive

copy sample data with
| aws s3 cp samples/ s3://serverless-data-pipeline-<UNIQUE-IDENT>/raw/ --recursive

send json-upload request through api
| curl https://xxxxxx.execute-api.us-east-1.amazonaws.com/dev/s3 -d samples/person1 -H 'Content-Type:application/json'


### Dash


## Credits


## References






