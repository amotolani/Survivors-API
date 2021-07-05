#!/bin/bash

set +xe

# Create function for running migrations
migrations() {
    python manage.py migrate
}

# Create function for Starting Server
start() {
    python manage.py runserver 0.0.0.0:8000
}

# Create function for super user creation
# Setting DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_USERNAME are required
create_superuser() {
    if [ -z "$DJANGO_SUPERUSER_PASSWORD" ] || [ -z "$DJANGO_SUPERUSER_USERNAME"  ] || [ -z "$DJANGO_SUPERUSER_EMAIL"  ]; then
      echo "Error: Undefined required parameters."
      echo "Help: Please define environment variables DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_USERNAME."
      exit 1
    else
      python manage.py createsuperuser --email "$DJANGO_SUPERUSER_EMAIL" --noinput
    fi

}

# Create function to initialise application with migrations, superuser creation and startup the server
init(){
  migrations
  create_superuser
  start
}

# validate script parameter and echo error if validation fails, provides help too
if [ "$1" != "migrations" ] && [ "$1" != "start" ] && [ "$1" != "init" ];then
  echo "Error: Invalid command."
  echo "Help: valid commands are 'migrations', 'start' and 'init'"
  exit 1
else
  $1
fi

