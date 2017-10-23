from flask import Flask
from flask import render_template

import datetime
import arrow
import boto3
import json
import configparser


def get_pipeline_status():
    """ Get Pipeline State From Config File
    http://boto3.readthedocs.io/en/latest/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_state
    Returns : Dictionary

     """
    # Set Keys from Config
    config = configparser.ConfigParser()
    config.sections()
    config.read('enviroment.ini')

    pipelinename = config['development']['pipelinename']

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
    data = get_pipeline_status()
    output = parse_pipeline_status(data)
    return render_template('index.html', title=output['Name'], blocks=output['Stages'])

@app.route("/test")
def dashboard_test():
    """ Dashboard Test Page """
    with open("sample.json") as json_data:
        # Load JSON File  and Mock Output
        data = json.load(json_data)
        for time_last in data['stageStates']:

            time_last['actionStates'][0]['latestExecution']['lastStatusChange'] = datetime.date.today()
        output = parse_pipeline_status(data)

    return render_template('index.html', title=output['Name'], blocks=output['Stages'])
