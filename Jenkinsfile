pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                echo 'Jenkins pulled the latest code from GitHub.'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline Passed: build and tests completed successfully.'
        }

        failure {
            echo 'CI Pipeline Failed: check the console output to find the problem.'
        }
    }
}