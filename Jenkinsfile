pipeline {
    agent { 
        docker.image('mbilgen/metacritic').withRun('-d -p 8090:8080')
         sh 'pwd ; ls -la'
        
    }
    stages {
        stage('Test Build') {
            steps {
                sh 'pwd ; ls -la'
                sh 'docker ps -a'
                //sh 'svn --version'
            }
        }
    }
}
