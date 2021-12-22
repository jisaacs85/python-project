pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(credentialsId: 'jenkins-deploy', branch: 'master', url: 'git@github.com:jisaacs85/python-project.git')
      }
    }

    stage('build') {
      steps {
        sh 'python *test.py'
      }
    }

  }
}