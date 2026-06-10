pipeline {
    agent any

    environment {
        APP_NAME = 'phase-2-jenkins-pipeline-lab'
        IMAGE_NAME = 'phase-2-jenkins-app'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from Git...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . .venv/bin/activate
                    ruff check app tests
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m pytest -v
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                    . .venv/bin/activate
                    bandit -r app
                    pip-audit
                '''
            }
        }

        stage('Build Container') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Deploy Simulation') {
            steps {
                withCredentials([string(credentialsId: 'demo-deploy-token', variable: 'DEPLOY_TOKEN')]) {
                    sh '''
                        chmod +x scripts/deploy-sim.sh
                        ./scripts/deploy-sim.sh
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Review the console output.'
        }

        always {
            echo 'Jenkins DevSecOps pipeline execution finished.'
        }
    }
}