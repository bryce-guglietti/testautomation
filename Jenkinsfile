pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'cd testautomation'
                sh 'cd tests'
                sh 'python run_tests.py'
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
