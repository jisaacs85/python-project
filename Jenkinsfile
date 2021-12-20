pipeline {
//    agent {
//        node {
//            label 'docker-jenkins'
//        }
//    }
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Code Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            parallel {
                stage('First Test') {
                    steps {
                        echo 'Run First Test here...'
                    }
                }
                stage('Second Test') {
                    steps {
                        echo 'Run Second Test here...'
                    }
                }
                stage('Python Test') {
                    steps {
                        echo 'Run Python Test here...'
                        sh 'python *test.py'
                    }
                }
            }
        }
    }
}
