#!/bin/bash

# Build the project
echo "Building the project..."
python3.7.5 -m pip install -r requirements.txt

echo "Make Migration..."
python3.7.5 manage.py makemigrations --noinput
python3.7.5 manage.py migrate --noinput

echo "Collect Static..."
python3.7.5 manage.py collectstatic --noinput --clear