pipeline {
  agent { 
    dockerfile true
  }
  stages { 
    stage('Example'){
      steps {
         echo 'Hello it is workin ;) ' 
         sh 'echo MetaCritic App Container was built...'
        sh 'docker ps -a'

      }
    }
   }   
}
