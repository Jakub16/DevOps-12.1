pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/your-repo-name.git'
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
