#!/bin/bash
# Migrate the database first
echo "Migrating the database before starting the server"
django-admin migrate

#collect static files at root directory
django-admin collectstatic --noinput

# Start Gunicorn processes
echo "Starting Gunicorn."
exec gunicorn -c './gunicorn_config.py' server.wsgi
