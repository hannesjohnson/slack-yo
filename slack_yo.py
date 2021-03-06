import os
import json
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST'])
def yo_handler():
    try:
        YO_API_TOKEN = os.environ['YO_API_TOKEN']
    except KeyError:
        return json.dumps({'text': 'Yo API token not set'})

    r = requests.post("http://api.justyo.co/yoall/", data={'api_token': YO_API_TOKEN})

    if 'result' in r.json() and r.json()['result'] == 'Error':
        return json.dumps({'text': 'Error sending Yo. Their API may be down, yo.'})
    else:
        return json.dumps({'text': 'Yo sent to team!'})

if __name__ == "__main__":
    app.run()