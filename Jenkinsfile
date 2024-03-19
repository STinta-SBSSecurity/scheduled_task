pipeline {
    agent any
    triggers {
        cron('H/3 * * * *') // Ejecutar cada 3 minutos
    }
    stages {
        stage('Call do_task') {
            steps {
                script {
                    sh "python3 do_task.py"
                }
            }
        }
 
    }
}