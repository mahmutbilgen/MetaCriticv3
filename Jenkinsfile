node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */
        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */   
        app = docker.build("mbilgen/metacritic")
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        app.inside {
            sh 'hostname;pwd;ls -la ;echo $PATH;netstat -tulpn'
            sh 'echo "Tests passed"'         
        }
    }

    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-cred') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
           echo "Trying to push docker build to Dockerhub ;)"
           echo " Envi.BUILD_ID : ${env.BUILD_ID}"
    }
    
    stage('Deploy image to Staging Server') {
        /* Finally, we'll pull  the newly built image into Staging Server :
         docker run -it -p 8080:8080 mbilgen/metacritic:latest*/
     
           /* docker {
                image 'mbilgen/metacritic:latest'
                args '-d -p 8090:8080'
            } */
           docker.image('mbilgen/metacritic:latest').withRun('-p 8090:8080') {
            /* do things */
               sh 'sleep 20 '
               sh 'curl localhost:8090/games'
           }
            //app.push("${env.BUILD_NUMBER}")
            //   app.pull("latest")
            
          // This step should not normally be used in your script. Consult the inline help for details.
          //withDockerContainer(args: '-p 8090:8080', image: 'mbilgen/metacritic') {
          // some block
          // }
           echo "Trying to pull docker build to Staging Server ;)"
           echo " Envi.BUILD_ID : ${env.BUILD_ID}"
    }
}
