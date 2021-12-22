pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(url: 'git@github.com:jisaacs85/python-project.git', branch: 'master', credentialsId: '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')
      }
    }

    stage('build') {
      steps {
        sh 'python *test.py'
      }
    }

  }
}