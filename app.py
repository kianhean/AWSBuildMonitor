from flask import Flask
from flask import render_template

import datetime
import arrow
import boto3
import json
import configparser

def loop_pipines(pipelines):
    """ Given List of Pipes, Return the Stages """
    pipes = []

    for pipe in pipelines:
        data = get_pipeline_status(pipe)
        output = parse_pipeline_status(data)

        pipes.append(output)

    return pipes


def get_pipeline_status(pipelinename):
    """ Get Pipeline State From Config File
    http://boto3.readthedocs.io/en/latest/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_state
    Returns : Dictionary

     """
    client = boto3.client('codepipeline')
    return client.get_pipeline_state(name=pipelinename)


def parse_pipeline_status(dict_data):
    """ Parse State Json """
    pipeline_name = dict_data['pipelineName']

    blocks = {}
    list_blocks = []

    # Compile Data
    for item in dict_data['stageStates']:
        blocks['name'] = item['actionStates'][0]['actionName']

        try:
            blocks['status'] = item['actionStates'][0]['latestExecution']['status']
        except:
            blocks['status'] = 'InProgress'

        try:
            blocks['percentage'] = item['actionStates'][0]['latestExecution']['percentComplete']
        except:
            blocks['percentage'] = 'Unknown'

        # Get Human Readable Arrow
        try:
            last = item['actionStates'][0]['latestExecution']['lastStatusChange']
            blocks['last'] = (arrow.get(last)).humanize()
        except:
            blocks['last'] = 'Never'

        if blocks['status'] == 'Failed':
            blocks['error_msg'] = item['actionStates'][0]['latestExecution']['errorDetails']['message']

        list_blocks.append(blocks.copy())

    return {'Name': pipeline_name, 'Stages':list_blocks}


app = Flask(__name__)


@app.route("/")
def dashboard():

    """ Dashboard Live Page """
    # Set Keys from Config
    config = configparser.ConfigParser()
    config.sections()
    config.read('enviroment.ini')

    pipelines = config['development']['pipelinename'].split(",")
    projectname = config['development']['projectname']
    refresh = config['development']['refresh']

    # Build List of Pipelines
    pipes = loop_pipines(pipelines)

    return render_template('pipeline.html', pipes=pipes, projectname=projectname, refresh=refresh)

@app.route("/local")
def dashboard_test():
    """ Dashboard Local Test Page """

    # Set Keys from Config
    config = configparser.ConfigParser()
    config.sections()
    config.read('enviroment.ini.sample')

    pipelines = config['development']['pipelinename'].split(",")
    projectname = config['development']['projectname']
    refresh = config['development']['refresh']

    # Gather Data for Local Page
    pipes = []

    for pipe in pipelines:
        with open("fixtures/" + pipe + ".json") as json_data:

            # Load JSON File  and Mock Output
            data = json.load(json_data)

            # Convert Datetime to Python Datetime to Simulate Boto3
            for time_last in data['stageStates']:
                time_last['actionStates'][0]['latestExecution']['lastStatusChange'] = datetime.date.today()
            output = parse_pipeline_status(data)
            pipes.append(output)

    return render_template('pipeline.html', pipes=pipes, projectname=projectname, refresh=refresh)
