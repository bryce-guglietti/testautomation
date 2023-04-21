pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'behave -f allure_behave.formatter:AllureFormatter -o ./allure-results ./features'
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
