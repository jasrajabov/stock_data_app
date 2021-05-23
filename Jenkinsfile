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
                        sh 'pip3 install -r requirements.txt --user'
                        echo 'Successfully installed packages!!!'
                        sh 'python3 -m py.test app/tests'
                    }
        }
                stage('Selenium') {
                    steps {
                        sh 'echo Executing feature tests'
                        sh 'python3 -m manage.py runserver'
                        sh 'Launched server!'
                        sh 'python3 -m py.test app/functional_tests/test_home_page.py'
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