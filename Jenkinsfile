pipeline {
    agent any
    triggers {
        cron(spec: 'H/1 * * * *') // Trigger cada 1 minuto
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
                expression{
                    expression { (new Date().getTime() - currentBuild.startTimeInMillis) / 1000 / 60 % 2 == 0 }
                }
            }
            steps {
                script {
                    sh "python3 hello.py"
                }
            }
        }
    }
}