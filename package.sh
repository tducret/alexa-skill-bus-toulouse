#!/bin/bash

# Based on an idea by https://github.com/voutilad/alexa-btvpython

# /!\ You need to make a virtualenv "skill" with :
# virtualenv skill
# source skill/bin/activate
# pip install ask-sdk

PACKAGE_NAME="alexa-skill-bus-toulouse"
PROJECT_DIR=$(pwd)
BUILD_DIR="build"
SOURCES="bus_toulouse.py tisseo.py"
VIRTUAL_ENV="skill"
NEEDED_PACKAGES="ask_sdk_core ask_sdk_model requests urllib3 certifi idna chardet pytz"
STOP_AREAS_FILE="stop_areas.json"

# Check if Tisseo API key is properly set to an environment variable
if [ -z "$TISSEO_API_KEY" ]
	then echo "TISSEO_API_KEY must be set to continue"
	exit 2
else
	rm "$STOP_AREAS_FILE"
	curl "http://api.tisseo.fr/v1/stop_areas.json?key=$TISSEO_API_KEY" > "$STOP_AREAS_FILE"
fi

# clear out existing package
mkdir -p ${BUILD_DIR}
rm -f "$BUILD_DIR/$PACKAGE_NAME.zip"

# package out python module
zip -r9 "$BUILD_DIR/$PACKAGE_NAME.zip" $SOURCES

# package dependencies
cd $VIRTUAL_ENV/lib/python3.7/site-packages
find . \( -name __pycache__ -o -name "*.pyc" \) -delete
zip -r9 "$PROJECT_DIR/$BUILD_DIR/$PACKAGE_NAME.zip" $NEEDED_PACKAGES
cd ${PROJECT_DIR}

# add necessary files
zip -r9 "$PROJECT_DIR/$BUILD_DIR/$PACKAGE_NAME.zip" "$STOP_AREAS_FILE"