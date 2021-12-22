pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(credentialsId: 'jisaacs85-git', branch: 'master', url: 'https://github.com/jisaacs85/python-project.git')
      }
    }

    stage('build') {
      steps {
        sh 'python *test.py'
      }
    }

  }
}