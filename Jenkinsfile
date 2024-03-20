pipeline {
    agent any
    triggers {
        cron(spec: 'H/1 * * * *', name: 'cron1') // cada 3 minutos
        cron(spec: 'H/3 * * * *', name: 'cron2') // cada 5 minutos
    }
    stages {
        stage('Call do_task') {
            when {
                expression{
                    currentBuild.getBuildVariables().get('TRIGGER_CAUSE')=='cron1'
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