import datetime
from flask import Flask
from flask_api import status
import json


app = Flask(__name__)
start_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/healthz')
def display_status():
    uptimemsg="up since {}".format(start_time)
    healthstatus=json.dumps({'status': status.HTTP_200_OK, 'version': "0.0.1", 'uptime': uptimemsg})
    return healthstatus

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

