#!/bin/bash

# Based on an idea by https://github.com/voutilad/alexa-btvpython

# /!\ You need to make a virtualenv "skill" with :
# virtualenv skill
# source skill/bin/activate
# pip install ask-sdk

PACKAGE_NAME="alexa-skill-bus-toulouse"
PROJECT_DIR=$(pwd)
BUILD_DIR="build"
SOURCE="bus_toulouse.py"
VIRTUAL_ENV="skill"
NEEDED_PACKAGES="ask_sdk_core ask_sdk_model"

# clear out existing package
mkdir -p ${BUILD_DIR}
rm -f "$BUILD_DIR/$PACKAGE_NAME.zip"

# package out python module and any dependencies installed in the virtual env
zip -r9 "$BUILD_DIR/$PACKAGE_NAME.zip" "$SOURCE"
cd $VIRTUAL_ENV/lib/python3.7/site-packages
find . \( -name __pycache__ -o -name "*.pyc" \) -delete
zip -r9 "$PROJECT_DIR/$BUILD_DIR/$PACKAGE_NAME.zip" $NEEDED_PACKAGES
cd ${PROJECT_DIR}