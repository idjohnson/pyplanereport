import requests
from flask import Flask, render_template
import os
from jinja2 import Environment, FileSystemLoader
import re

app = Flask(__name__)

projectid = os.environ.get("PRJID")
workspacename = os.environ.get("WSNAME")
planeapikey = os.environ.get("APIKEY")
tableTitle = os.environ.get("TABLETITLE")
ignoreState = os.environ.get("IGNORESTATE")

# check if csv a contains b
def check_string_in_list(a, b):
    return any(e in b for e in a.split(','))

@app.route('/')
def index():
    url = f'https://api.plane.so/api/v1/workspaces/{workspacename}/projects/{projectid}/issues/'
    headers = {
        'X-API-Key': planeapikey,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    results = data['results']


    urlstates = f'https://api.plane.so/api/v1/workspaces/{workspacename}/projects/{projectid}/states/'
    stateresponse = requests.get(urlstates, headers=headers)
    statedata = stateresponse.json()
    stateresults = statedata['results']
    
    table_data = []
    for result in results:
        description_html = re.sub(":: Requested by.*", "", result['description_html'])
        stateName = ""
        for state in stateresults:
           if state["id"] == result['state']:
               stateName = state["name"]
        if not check_string_in_list(ignoreState,stateName):
           table_data.append([result['name'], stateName, description_html, result['target_date']])
    env = Environment(loader=FileSystemLoader('/app'))
    template = env.get_template('table.html')
    return template.render(table_data=table_data,title=tableTitle)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

