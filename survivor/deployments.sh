#!/bin/bash

set +xe

# Create function for build/tagging application image
build() {
    docker build -t devopzguru/survivorapi:1.0 .
}

push() {
    docker login --username devopzguru --password 70d38107-6b86-42ad-976d-669121010956
    docker push devopzguru/survivorapi:1.0
}
# create function to seed test data into docker-compose deployment
compose-seed() {
    docker exec -it survivor_survivor-service_1 python manage.py loaddata passengers.json
}
# create function to setup kibana index in docker-compose deployment
compose-kibana-init() {
    docker exec -it survivor_survivor-service_1 python elk/index-pattern.py
}

# create function to seed test data into kubernetes deployment
kubernetes-seed() {
    kubectl exec -it deploy/survivor-deployment -- python manage.py loaddata passengers.json
}

# create function to setup kibana index in kubernetes deployment
kubernetes-kibana-init() {
    kubectl exec -it deploy/survivor-deployment -- python elk/index-pattern.py
}

# Create function for converting .env file to kubernetes secret manifest
secret_templating() {
    cp .env templates
    docker build -t templates:1.0 -f templates/Dockerfile templates
    docker run -v /Users/dadelowo/Documents/out:/tmp/out templates:1.0
    cp /Users/dadelowo/Documents/out/kubernetes-secrets.yml .
}

# Create function for deploying application
deploy() {
    echo "Deployment Options."
    echo "Enter '1' to deploy using docker-compose"
    echo "Enter '2' to deploy using kubernetes"
    echo -n "Your Answer: "
    read -r deployment_choice

    if [ "$deployment_choice" == 1 ]; then
      echo '..............Building Application Image................'
      echo '........................................................'
      build
      chmod -R 777 ./elk
      echo '....... Deploying application with docker compose.......'
      echo '........................................................'
      docker-compose up -d
      echo '................Application Initializing.................'
      echo '....................Setup Complete.......................'
    elif [ "$deployment_choice" == 2 ]; then
      echo '..............Building Application Image................'
      echo '........................................................'
      build
      echo '........Pushing application with docker registry........'
      echo '........................................................'
      push
      echo '.........Creating your application apps secrets.........'
      echo '........................................................'
      secret_templating
      kubectl apply -f kubernetes-secrets.yml
      echo '..........Deploying application to your cluster..........'
      echo '.........................................................'
      kubectl apply -f kubernetes.yml
      echo '....................Setup Complete.......................'
    else
      echo "Invalid Option selected."
      exit 1
    fi

}

# Create function for destroying application deployment
destroy() {
    echo "## WARNING...YOU ARE ABOUT TO DESTROY YOUR DEPLOYMENT !!! ##"
    echo " "
    echo "Enter '1' to remove docker-compose deployment"
    echo "Enter '2' to remove kubernetes deployment"
    echo -n "Your Answer: "
    read -r deployment_choice
    echo -n "Enter 'yes' to confirm: "
    read -r confirm

    if [ "$confirm" == 'yes' ]; then
      if [ "$deployment_choice" == 1 ]; then
        echo '...........Destroying application deployment............'
        echo '........................................................'
        docker-compose down
      elif [ "$deployment_choice" == 2 ]; then
        echo '...........Destroying application deployment............'
        echo '........................................................'
        kubectl delete -f kubernetes.yml
        kubectl delete -f kubernetes-secrets.yml
      else
        echo "Invalid Option selected."
        exit 1
      fi
    else
      echo "Operation Cancelled.."
    fi
}

# Create function for deploying application
seed() {
    echo "Seeding Options."
    echo "Enter '1' to seed data into your docker-compose deployment"
    echo "Enter '2' to seed data into your kubernetes deployment"
    echo -n "Your Answer: "
    read -r seeding_choice

    if [ "$seeding_choice" == 1 ]; then
      compose-seed
    elif [ "$seeding_choice" == 2 ]; then
      kubernetes-seed
    else
      echo "Invalid Option selected."
      exit 1
    fi

}

# validate script parameter and echo error if validation fails, provides help too
if [ "$1" == "deploy" ];then
  deploy
elif [ "$1" == "destroy"  ];then
  destroy
elif [ "$1" == "seed"  ];then
  seed
else
  echo "Error: Invalid command."
  echo "Help: valid commands are 'deploy', 'destroy' and 'seed'"
  exit 1
fi
