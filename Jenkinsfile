pipeline {
    agent any
    triggers {
        cron('H/2 * * * *') // Ejecutar cada 3 minutos
        cron('H/3 * * * *') // Ejecutar cada 3 minutos
    }
    stages {
        stage('Call do_task') {
            when {
                expression{
                    currentBuild.getBuildVariables().get('TRIGGER_CAUSE')=='cron'
                }
            }
            steps {
                script {
                    sh "python3 do_task.py"
                }
            }
        }
        stage('Call hello') {
            when {
                expression{
                    currentBuild.getBuildVariables().get('TRIGGER_CAUSE')=='cron2'
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