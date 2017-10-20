### Work In Progress for a build monitor for AWS Code Pipeline

# Config AWS Cred
aws configure

# Add enviroment.ini with pipeline name

# Run
FLASK_APP=hello.py flask run


# Dev Notes
# init pipenv
pipenv --python 3.6

# activiting virtualenv
pipenv shell
FLASK_APP=hello.py flask run

# Run Tests
python -m unittest
