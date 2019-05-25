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
  serviceAccountName: jenkins
  containers:
  - name: python
    image: python:3.7
    command:
    - cat
    tty: true
  - name: helm
    image: lachlanevenson/k8s-helm:v2.14.0
    command:
    - cat
    tty: true
"""
        }
    }
    stages {
        stage('Build') {
            steps {
                container('python') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                container('python') {
                    sh 'pytest --cov=.'
                }
            }
        }
        stage('Deploy') {
            steps {
                container('helm') {
                    sh 'helm ls'
                }
            }
        }
    }
}
