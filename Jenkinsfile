pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python tests/run_tests.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
