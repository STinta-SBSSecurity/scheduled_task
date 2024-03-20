pipeline {
    agent any
    triggers {
        cron(spec: 'H/30 * * * *', label: 'cron1') // Trigger cada 30 minutos
    }
    triggers {
        cron(spec: 'H/15 * * * *', label: 'cron2') // Otro trigger cada 15 minutos
    }
    
}