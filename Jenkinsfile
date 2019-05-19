pipeline {
agent {
  docker {
    args '-d -p 8090:8080'
    image 'mbilgen/metacritic'
    label 'latest'
  }
}
    
    stages {
        stage('Test Build') {
            steps {
                sh 'pwd ; ls -la'
                sh '/usr/bin/docker ps -a'
                //sh 'svn --version'
            }
        }
    }
}
