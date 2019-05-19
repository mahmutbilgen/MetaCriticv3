pipeline {
    agent {
        docker {
           image 'mbilgen/metacritic'
          // label 'my-defined-label'
           args  '-d -p 8090:8080'
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
