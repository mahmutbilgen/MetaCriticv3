pipeline {
    agent { 
        docker {            
            image 'mbilgen/metacritic'
            args '-d -p 8090:8080'
        }
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
