#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

def generate_matrix():
    """
    Generates a GitHub Actions matrix.

    This can be expanded in the future to use dependencies from the Nix flake,
    for example, using boto3 to query AWS for a list of environments to test against.
    """
    # For now, a static list.
    environments = [

        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'airbyte--connectors'},
        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'airbyte--connectors-postgres'},
        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'airbyte--iam--kinesis-user'},
        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'airbyte--rds'},
        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'airbyte--rds-users'},
        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'airbyte--s3--logs'},
        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'bastion-server'},
        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'bde--client-export-cloudfront'},
        {'env': 'dev', 'region': 'us-east-2', 'deployment': 'bi--iam--etl-datalake'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'bi--rds'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'bi--rds-real-time-etl'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'bi--rds-real-time-etl-users'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'bi--rds-users'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'breeze'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'capiq--opensearch'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'cloudwatch-alarms'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'dataservice--opensearch'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'genai--document-db'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'genai--elasticache'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'genai--irsa'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'genai--s3-genera-data'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'k8s--resources'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'lease--s3--data-transfer'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'looker-bastion'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'mv--data-report'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'mv--db'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'mv--k8s'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'mwaa'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'pagerduty'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'pc--iam--rds-export'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'rise--iam--acs-datalake'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'sandcastle--elasticache'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'sandcastle--rds'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'sandcastle--rds-users'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'sandcastle--route53-acm'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'sandcastle--s3--datalake'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'sandcastle--track-sc-client-changes'},
        {'env': 'dev', 'region': 'us-east-1', 'deployment': 'sandcastle-data-ingestion--s3'},
        
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'airbyte--connectors'},
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'airbyte--connectors-postgres'},
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'airbyte--iam--kinesis-user'},
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'airbyte--rds'},
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'airbyte--rds-users'},
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'airbyte--s3--logs'},
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'bastion-server'},
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'bde--client-export-cloudfront'},
        {'env': 'stg', 'region': 'us-east-2', 'deployment': 'bi--iam--etl-datalake'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'bi--rds'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'bi--rds-real-time-etl'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'bi--rds-real-time-etl-users'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'bi--rds-users'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'breeze'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'capiq--opensearch'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'cloudwatch-alarms'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'dataservice--opensearch'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'genai--document-db'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'genai--elasticache'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'genai--irsa'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'genai--s3-genera-data'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'k8s--resources'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'lease--s3--data-transfer'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'looker-bastion'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'mv--data-report'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'mv--db'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'mv--k8s'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'mwaa'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'pagerduty'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'pc--iam--rds-export'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'rise--iam--acs-datalake'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'sandcastle--elasticache'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'sandcastle--rds'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'sandcastle--rds-users'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'sandcastle--route53-acm'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'sandcastle--s3--datalake'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'sandcastle--track-sc-client-changes'},
        {'env': 'stg', 'region': 'us-east-1', 'deployment': 'sandcastle-data-ingestion--s3'},

        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'airbyte--connectors'},
        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'airbyte--connectors-postgres'},
        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'airbyte--iam--kinesis-user'},
        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'airbyte--rds'},
        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'airbyte--rds-users'},
        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'airbyte--s3--logs'},
        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'bastion-server'},
        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'bde--client-export-cloudfront'},
        {'env': 'prd', 'region': 'us-east-2', 'deployment': 'bi--iam--etl-datalake'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'bi--rds'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'bi--rds-real-time-etl'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'bi--rds-real-time-etl-users'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'bi--rds-users'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'breeze'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'capiq--opensearch'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'cloudwatch-alarms'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'dataservice--opensearch'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'genai--document-db'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'genai--elasticache'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'genai--irsa'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'genai--s3-genera-data'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'k8s--resources'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'lease--s3--data-transfer'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'looker-bastion'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'mv--data-report'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'mv--db'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'mv--k8s'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'mwaa'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'pagerduty'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'pc--iam--rds-export'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'rise--iam--acs-datalake'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'sandcastle--elasticache'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'sandcastle--rds'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'sandcastle--rds-users'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'sandcastle--route53-acm'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'sandcastle--s3--datalake'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'sandcastle--track-sc-client-changes'},
        {'env': 'prd', 'region': 'us-east-1', 'deployment': 'sandcastle-data-ingestion--s3'},

    ]
    
    matrix = {'include': environments}
    json_obj = json.dumps(matrix)

    github_output_file = os.getenv("GITHUB_OUTPUT")
    if github_output_file:
        with open(github_output_file, "a") as f:
            print(f'matrix={json_obj}', file=f)
    else:
        print(json_obj)

if __name__ == "__main__":
    generate_matrix() 