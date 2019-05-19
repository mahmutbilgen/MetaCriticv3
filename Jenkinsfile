pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'pwd ; ls -la'
                sh 'docker ps -a'
                //sh 'svn --version'
            }
        }
    }
}
