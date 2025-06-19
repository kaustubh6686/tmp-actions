#!/bin/bash

# check if env is set
if [ -z "$BRANCH_MASTER" ]; then
    $BRANCH_MASTER = "master"
fi

if [ -z "$BRANCH_STAGING" ]; then
    $BRANCH_STAGING = "staging"
fi

if [ -z "$BRANCH_PRODUCTION" ]; then
    $BRANCH_PRODUCTION = "production"
fi

echo "BRANCH_MASTER: $BRANCH_MASTER"
echo "BRANCH_STAGING: $BRANCH_STAGING"
echo "BRANCH_PRODUCTION: $BRANCH_PRODUCTION"