pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(url: 'https://github.com/jisaacs85/python-project.git', branch: 'master', credentialsId: 'jisaacs85-git')
      }
    }

    stage('build') {
      steps {
        sh 'python *test.py'
      }
    }

  }
}