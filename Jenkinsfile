pipeline {
  agent any
  stages {
    stage('') {
      steps {
        git(url: 'git@github.com:jisaacs85/python-project.git', branch: 'master', credentialsId: 'jisaacs85-git')
      }
    }

    stage('build') {
      steps {
        sh 'python *test.py'
      }
    }

  }
}