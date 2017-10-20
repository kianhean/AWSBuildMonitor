# Work In Progress for a build monitor for AWS Code Pipeline

Quick and dirty way to get something better looking than the default


### Config AWS Cred
aws configure

### Edit enviroment.ini
Add enviroment.ini with pipeline name

### Run
FLASK_APP=hello.py flask run


# Dev Notes
### init pipenv
pipenv --python 3.6

### activiting virtualenv
pipenv shell
FLASK_APP=hello.py flask run

### Run Tests
python -m unittest
