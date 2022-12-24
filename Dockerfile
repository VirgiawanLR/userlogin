# execute this dockerfile for building docker image custom based on existing docker image
# python:3.10-buster is the existing docker image on this case 

from python:3.10-buster

run apt update

workdir /app
# given name of the desire working directory to applied on
copy . /app
# copying all the files in current main host directory to the /app docker image directory 
run pip install flask-restful \
    pip install python-dotenv \
    pip install mysql-connector-python

cmd ["python3", "main.py"]