FROM python:3.12-slim

WORKDIR /flask-app 

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt 

COPY . . 

# ENV FLASK_APP=blueprint_app

WORKDIR /flask-app/blueprint_app 

RUN flask db init 
RUN flask db migrate 
RUN flask db upgrade 

WORKDIR /flask-app 

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]

