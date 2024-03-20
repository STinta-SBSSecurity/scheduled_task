pipeline {
    agent any
    triggers {
        cron('H/3 * * * *') // Trigger cada 1 minuto
    }
    stages {
        stage('Call do_task') {
            steps {
                script {
                    sh "python3 do_task.py"
                }
            }
        }
        stage('Espera 2 minutos') {
            steps {
                script {
                    sleep 120
                }
            }
        }
        stage('Call hello') {
            steps {
                script {
                    sh "python3 hello.py"
                }
            }
        }
    }
}