#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

deployments = [
    'airbyte--connectors',
    'airbyte--connectors-postgres',
    # 'airbyte--iam--kinesis-user',
    # 'airbyte--rds',
    # 'airbyte--rds-users',
    # 'airbyte--s3--logs',
    # 'bastion-server',
    # 'bde--client-export-cloudfront',
    # 'bi--iam--etl-datalake',
    # 'bi--rds',
    # 'bi--rds-real-time-etl',
    # 'bi--rds-real-time-etl-users',
    # 'bi--rds-users',
    # 'breeze',
    # 'capiq--opensearch',
    # 'cloudwatch-alarms',
    # 'dataservice--opensearch',
    # 'genai--document-db',
    # 'genai--elasticache',
    # 'genai--irsa',
    # 'genai--s3-genera-data',
    # 'k8s--resources',
    # 'lease--s3--data-transfer',
    # 'looker-bastion',
    # 'mv--data-report',
    # 'mv--db',
    # 'mv--k8s',
    # 'mwaa',
    # 'pagerduty',
    # 'pc--iam--rds-export',
    # 'rise--iam--acs-datalake',
    # 'sandcastle--elasticache',
    # 'sandcastle--rds',
    # 'sandcastle--rds-users',
    # 'sandcastle--route53-acm',
    # 'sandcastle--s3--datalake',
    # 'sandcastle--track-sc-client-changes',
    # 'sandcastle-data-ingestion--s3',
    # 'shared--aws-backup-vault',
    # 'shared--datadog',
    # 'shared--eks-data-insights',
    # 'shared--eks-emr',
    # 'shared--eks-emr-spark',
    # 'shared--eks-main',
    # 'shared--iam--bulk-export',
    # 'shared--iam--data-sharing',
    # 'shared--iam--users',
    # 'shared--oidc-provider',
    # 'shared--rds-access',
    # 'shared--s3--athena-storage',
    # 'shared--s3--cost-budget',
    # 'shared--s3--datalake',
    # 'shared--s3--dbt-artifacts',
    # 'shared--s3--emr-jars',
    # 'shared--s3--vts-client-export',
    # 'shared--snowflake',
    # 'shared--snowflake-legacy',
    # 'shared--snowflake-legacy-unico',
    # 'snowflake',
    # 'snowflake--legacy--iam-datalake',
    # 'tenant-linking--rds',
]

def generate_matrix():
    """
    Generates a GitHub Actions matrix.

    This can be expanded in the future to use dependencies from the Nix flake,
    for example, using boto3 to query AWS for a list of environments to test against.
    """
    # For now, a static list.
    environments = {}

    for env in ['dev', 'stg', 'uat', 'prd']:
        environments[env] = {'include': []}

        if env == 'uat':
            continue

        for region in ['us-east-2', 'us-west-2']:
            for deployment in deployments:
                environments[env]['include'].append({'env': env, 'region': region, 'deployment': deployment})
    
    matrix = environments
    json_obj = json.dumps(matrix)

    github_output_file = os.getenv("GITHUB_OUTPUT")
    if github_output_file:
        with open(github_output_file, "a") as f:
            print(f'matrix={json_obj}', file=f)
    else:
        print(json_obj)

if __name__ == "__main__":
    generate_matrix() 