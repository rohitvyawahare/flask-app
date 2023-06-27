#Deploy Flask Application on Kubernetes using - Jenkins + Git + Kubernetes
----------------------------------------------------------------------------

## Project Description
This project focuses on automating the deployment of a Flask web application on a Kubernetes cluster using Jenkins. The application is containerized using Docker, and the Docker images are pushed to Docker Hub.

This application produce a Hello World msg and also query with postgres database and print user' name

## Prerequisites
Before proceeding with the installation, ensure that you have the following prerequisites:
- Kubernetes cluster with at least 4 nodes
- Jenkins host with proper configuration
- Git
- Docker
- Docker Hub account


## Directory Structure
- Dockerfile -->> docker file to build flask app image
- Jenkinsfile -->> to automate build and deploy process
- app.py -->> contains applicaton code
- config.cfg -->> store postgres DB creds 
- deployment.yaml -->> menifest file to deploy resources on kubernetes cluster
- entrypoint.sh -->> contains entrypoint command to run a container
- requirements.txt -->> store all the dependencies to run application


## Steps:-
1-->> Push this code into your github repo

2-->> you need to setup kubernetes cluster

3-->> then install and configure jenkins master on a node 

4-->> setup a jenkins agent node and configure that node into jenkins master

5-->> install all the neccesary plugins [ Eg.  docker' plugin, kubernetes' plugin ]

6-->> configure all the credential into jenkins credential manager

7-->> i configured dockerhub creds, github creds, and seted up kubeconfig file on jenkinshost to interact with kubernetes API

8-->> I created a job with with name flask-app and configured the source as my github repo https://github.com/rohitvyawahare/flask-app.git

9-->> i created a Jenkinsfile, that file clone the repo and build the image using existing docker file

10-->> then it will push that image to my dockerhub repo "docker.io/rohir/flask-app" 

11-->> now jenkins will run a command that command will apply deployment.yaml onto my cluster

12-->> that deployment file will create 2 deployment with name flask and postgres with 1 replica of each

13-->> also it will create configmap to store DB creds and DB name ( i havn't use secret here, use secret for best practice )

14-->> it will create 2 service, one for flask-app ( nodeport type with 30500 port )  and  second for postgres ( clusterip )

15-->> now we can access our flask application with http://workernodeIP:30500/test [ it will print a msg hello world i am rohit ]

16-->> when you access http://workernodeIP:30500/test_db [ it will query to database and print msg User Rohit from database ]

## Author
Rohit Sanjay Vyawahare
rohitvyawahare04@gmail.com
