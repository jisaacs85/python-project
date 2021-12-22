pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(credentialsId: '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', url: 'git@github.com:jisaacs85/python-project.git', branch: 'master')
      }
    }

    stage('build') {
      steps {
        sh 'python *test.py'
      }
    }

  }
}