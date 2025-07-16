#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Collect static files (optional but useful for admin and CSS)
python manage.py collectstatic --noinput
