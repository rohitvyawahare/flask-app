pipeline {
  environment {
    dockerimagename = "rohir/flask-app"
    dockerImage = ""
  }
  agent any
  stages {
    stage('Checkout Source') {
      steps {
        git 'https://github.com/rohitvyawahare/flask-app.git'
      }
    }
    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build dockerimagename
        }
      }
    }
    stage('Pushing Image') {
      environment {
               registryCredential = 'docker-hub-creds'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            dockerImage.push("latest")
          }
        }
      }
    }
    stage('Deploying webapp to Kubernetes') {
      steps {
        script {
          sh 'kubectl apply -f deployment.yaml'
        }
      }
    }
  }
}

