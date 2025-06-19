#!/bin/bash

# check if env is set
if [ -z "$BRANCH_MASTER" ] || [ "$BRANCH_MASTER" == "" ]; then
    BRANCH_MASTER="master"
fi

if [ -z "$BRANCH_STAGING" ] || [ "$BRANCH_STAGING" == "" ]; then
    BRANCH_STAGING="staging"
fi

if [ -z "$BRANCH_PRODUCTION" ] || [ "$BRANCH_PRODUCTION" == "" ]; then
    BRANCH_PRODUCTION="production"
fi

if [ -z "$TEST_TAG" ] || [ "$TEST_TAG" == "" ]; then
    TEST_TAG="5.219.0"
fi

echo "BRANCH_MASTER: $BRANCH_MASTER"
echo "BRANCH_STAGING: $BRANCH_STAGING"
echo "BRANCH_PRODUCTION: $BRANCH_PRODUCTION"
echo "TEST_TAG: $TEST_TAG"