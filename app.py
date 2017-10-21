from flask import Flask
from flask import render_template


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

    client = boto3.client(pipelinename)
    return client.get_pipeline_state(pipelinename)


def parse_pipeline_status(dict_data):
    """ Parse State Json """
    pipeline_name = dict_data['pipelineName']
    stages = dict_data['stageStates']

    return {'Name': pipeline_name, 'Stages':stages}


app = Flask(__name__)


@app.route("/")
def dashboard():
    """ Dashboard Live Page """
    data = get_pipeline_status()
    output = parse_pipeline_status(data)
    return render_template('index.html', title=output['Name'])

@app.route("/test")
def dashboard_test():
    """ Dashboard Test Page """
    with open("sample.json") as json_data:
        data = json.load(json_data) # Load JSON File
        output = parse_pipeline_status(data)
    return render_template('index.html', title=output['Name'])
