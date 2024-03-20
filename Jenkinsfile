pipeline {
    agent any
    triggers {
        cron('*/3 * * * *') // cada 3 minutos
    }
    stages {
        stage('Stages Paralelos') {
            parallel {
                stage('Call do_task') {
                    steps {
                        script {
                            sh "python3 do_task.py"
                        }
                    }
                }
                stage('Call hello') {
                    steps {
                        script {
                            // Si es la primera ejecución del pipeline
                            if (currentBuild.number == 1) {
                                echo 'Segundo stage ejecutándose en paralelo en la primera corrida'
                            } else {
                                // Esperar 5 minutos (300 segundos)
                                sleep 300
                            }
                            def horaEjecucion = new Date()
                            echo "Hora de ejecución del segundo stage: ${horaEjecucion}"
                            sh "python3 hello.py"

                        }
                    }
                }
            }
        }
    }
}
