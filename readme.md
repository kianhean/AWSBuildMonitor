# Build monitor for AWS Code Pipeline
Quick and dirty way to get something better looking than the default!

![screens](https://user-images.githubusercontent.com/5037305/32870256-f684fe9e-cab5-11e7-9d69-1ef4798d24c2.png)

## Feature Support

- No Other AWS Code Pipeline BuildMonitor that i know of
- Support Multiple or Single AWS Code Pipelines
- Support Multiple or Single Build Steps
- Progress Bar for each Build Step
- BootStrap 4 + FontAwesome Goodness!

## Local Installation
### Clone this Repo
git clone https://github.com/kianhean/AWSBuildMonitor.git

```bash
pipenv install
```

### Config AWS Credentials
Intall AWS CLI on computer

Run 

```
aws configure
```

Ensure that credentials have sufficient permissions, namely "get_pipeline_state" for the resource in question.

### Edit enviroment.ini
Edit the enviroment.ini.sample and save file as enviroment.ini

```bash
projectname = The Name of Your Project
pipelinename = Name of your Piplines Seperated by Commas
refresh = Number of seconds to wait before a force a forced refresh of the monitor
```

### Run
```bash
pipenv shell

FLASK_APP=app.py flask run
```

# Dev Notes
#### init pipenv

```bash
pipenv --python 3.6
```

#### activiting virtualenv

```bash
pipenv shell
FLASK_APP=app.py flask run
```

#### Run Tests
```bash
python -m unittest
```
