FROM python:3.8

WORKDIR /stock_data_app

COPY . ./my_django_app

CMD ["ls"]

RUN pip install -r ./my_django_app/requirements.txt

#CMD ["py.test", "./my_django_app/app/tests/"]

#CMD ["py.test", "./my_django_app/app/functional_tests/"]


#Steps
#1. docker build -t imagename path --> creating image
#2. docker run imagename --> running docker image