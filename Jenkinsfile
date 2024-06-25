pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Jakub16/DevOps-12.1.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }

    post {
        always {
            junit 'test-reports/*.xml'
        }
    }
}
