pipeline {
    agent any
    triggers {
        cron('H/1 * * * *') // Trigger cada 1 minuto
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
                    sleep 120 // Espera 5 minutos (300 segundos)
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