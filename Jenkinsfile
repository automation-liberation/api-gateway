pipeline {
    agent {
    kubernetes {
      label 'api-gateway'
      defaultContainer 'python'
      yaml """
apiVersion: v1
kind: Pod
metadata:
labels:
  component: ci
spec:
  serviceAccountName: zeroed-quetzal-jenkins
  containers:
  - name: python
    image: python:3.7
    command:
    - cat
    tty: true
"""
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'apt install pipenv'
        sh 'pipenv install'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest --cov=.'
      }
    }
  }
}
