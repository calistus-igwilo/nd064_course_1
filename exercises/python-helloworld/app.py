from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():

    # add log line
    app.logger.info("Main request successful")

    return "Hello World! Added endpoint"

@app.route("/status")
def checkStatus():
    response = app.response_class(
        response = json.dumps({'result':"Ok - Healthy"}),
        status = 200,
        mimetype = 'application/json'
    )

    ## add log line
    app.logger.info("Status request successful")

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
        response = json.dumps({'status':'success', 'code':0, 'data': {'UserCount':140, 'UserCountActive':23}}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info("Metrics request successful")

    return response

if __name__ == "__main__":

    ## Stream logs to app.log file
    logging.basicConfig(filename = 'app.log', level = logging.DEBUG)
    
    app.run(host='0.0.0.0')

