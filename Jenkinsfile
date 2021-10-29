pipeline {
    agent any
    environment {
	    /* tag is the last commit id to be used as tag for the docker container image */
        TAG=sh (
            returnStdout: true,
            script: 'git describe --tags --always'
        ).trim()
		/* branch tag will be jenkins environment variable storing the branch name */
        BRANCH_TAG=sh (
            returnStdout: true,
            script: 'echo ${GIT_BRANCH} | cut -d "/" -f 2'
        )
		DOCKERFILE_NAME="Dockerfile"
    }
    stages {
        stage('git checkout') {
            steps {
                /* this clones the repository under the workspace */		
                checkout scm
            }
        }
        stage('build image') {
            steps {
                script{
				    /* image tag to be kept, dockerfile_name to be kept in environmental variables*/
                    image = docker.build("2233445566a/unittest_main:${TAG}", "-f ${DOCKERFILE_NAME} .")
                }
            }
        }
        stage('unit_testing') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                sh 'python3 test_main.py'    
                }
            }
        }
	    stage('test echo') {
            steps {
                echo "test completed"
            }
        }
    }
}
