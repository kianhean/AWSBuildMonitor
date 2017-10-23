# Build monitor for AWS Code Pipeline (WIP)
Quick and dirty way to get something better looking than the default

![screens](https://user-images.githubusercontent.com/5037305/31896530-9958ee8c-b846-11e7-920f-17562fae6af9.png)

### Clone this Repo
git clone https://github.com/kianhean/AWSBuildMonitor.git

pipenv install

pipenv shell

### Config AWS Cred
aws configure

### Edit enviroment.ini
Add enviroment.ini.sample with pipeline name and save file as enviroment.ini

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
