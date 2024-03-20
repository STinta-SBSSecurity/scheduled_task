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
        stage('Call hello') {
            when {
                timeout(time: 2, unit: 'MINUTES')
            }
            steps {
                script {
                    sh "python3 hello.py"
                }
            }
        }
    }
}