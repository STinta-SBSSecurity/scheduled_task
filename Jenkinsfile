pipeline {
    agent any
    triggers {
        cron('H/2 * * * *') // Trigger cada 1 minuto
    }
    stages {
        stage('Call do_task') {
            steps {
                script {
                    sh "python3 do_task.py"
                }
            }
        }
        stage('Espera 4 minutos') {
            steps {
                script {
                    sleep 240
                }
            }
        }
        stage('Call hello') {
            steps {
                script {
                    def horaEjecucion = new Date()
                    echo "Hora de ejecución del segundo stage: ${horaEjecucion}"
                    sh "python3 hello.py"
                }
            }
        }
    }
}