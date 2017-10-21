# Build monitor for AWS Code Pipeline (WIP)
Quick and dirty way to get something better looking than the default

![screens](https://user-images.githubusercontent.com/5037305/31853950-42776892-b6c4-11e7-98e4-8c72a311febe.png)

### Config AWS Cred
aws configure

### Edit enviroment.ini
Add enviroment.ini with pipeline name

### Run
FLASK_APP=app.py flask run


# Dev Notes
### init pipenv
pipenv --python 3.6

### activiting virtualenv
pipenv shell
FLASK_APP=app.py flask run

### Run Tests
python -m unittest
