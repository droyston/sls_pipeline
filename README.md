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

- boto3: AWS S3 interaction

### Processing Logic


### Data Source


## Deployment


serverless data pipeline demployment demo

inspired by https://towardsdatascience.com/build-a-serverless-data-pipeline-on-aws-7c7d498d9707


requires serverless and appropriately permissioned AWS roles

these roles must be inserted into 'serverless.yml' in the ROLE and GLUE-ROLE fields

deploy with 
| sls deploy --stage <UNIQUE-IDENT>


send PUT commands with Postman


## Credits


## References






