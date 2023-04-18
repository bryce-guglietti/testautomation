pipeline {
    agent any

    stages {
        stage('Install Allure') {
            steps {
                bat 'curl -o allure-2.14.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.tgz'
                bat 'tar -zxvf allure-2.14.0.tgz'
                bat 'export PATH=$PATH:$(pwd)/allure-2.14.0/bin'
                bat 'allure --version'
            }
        }
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
