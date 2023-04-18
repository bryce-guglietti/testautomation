pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python tests/run_tests.py'
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
    post{
        always{
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    
    }
}
