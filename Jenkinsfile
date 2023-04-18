pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python testautomation/tests/run_test.py'
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
