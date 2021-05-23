pipeline {
    agent any
    triggers {
    //runs every 15 min between 1-2 pm every weekend
        cron('H/30 13-14 * * 6-7')
    }
    stages {
        stage('Tests') {
            parallel {
                stage('Pytest') {
                    steps {
                        echo 'Executing pytest unittest'
                        sh 'ls'
                        sh 'source venv/bin/activate'
                        sh 'pip3 install -r requirements.txt --user'
                        sh 'python3 -m pytest app/tests'
                    }
        }
                stage('Selenium') {
                    steps {
                        sh 'echo Executing feature tests'
                        sh 'python3 -m app/functional_tests'
                    }
                }
    }
        }
    }
    post {
        always {
            emailext body: 'BUILD STATS: $DEFAULT_CONTENT',
            subject: '$DEFAULT_SUBJECT',
            to: 'razhabov@yahoo.com'
            }
        }
    }
}