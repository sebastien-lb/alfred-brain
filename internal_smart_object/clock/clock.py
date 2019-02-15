import time
import schedule
import sys
import requests
from os import listdir, system
from datetime import datetime

from flask import Flask, json, request
from threading import Thread

app = Flask(__name__)

# rounded (and sent) every {ROUND_TIME} seconds
ROUND_TIME = 10

def send_status_if_round_time():
    print(int(time.time()))
    if int(time.time()) % ROUND_TIME == 0:
        send_status()

def send_status():
    data = {}
    # for now we only send the temp without the celsius
    data["value"] = int(time.time())
    print("Sending Status", data["value"])

    with open("server.json", "r") as file:
        server = json.loads(file.read())
        data["data_source_id"] = server["data-source-ids"]["clock"]

    requests.post("http://" + server["url"] + ":" + server["port"] + "/saveDataPoint", data=json.dumps(data),
                  headers={'Content-type': 'application/json'})

    return app.response_class(status=200)


@app.route('/serverConfig', methods=['POST'])
def setServerConfig():
    try:
        data = request.get_json(force=True)
        server_config = {}
        server_config["url"] = data.get("url")
        server_config["id"] = data.get("id")
        server_config["port"] = data.get("port")
        server_config["data-source-ids"] = data.get("data-source-ids")
    except:
        return app.response_class(status=400)


    with open("server.json", "w") as file:
        file.write(json.dumps(server_config))

    response = app.response_class(
        status=200
    )
    return response

@app.route('/time')
def getTime():
    data = datetime.utcnow()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/config')
def getConfigResponse():
    data = {}
    with open("config.json") as file:
        data = json.loads(file.read())
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response

def runJobs():
    while True:
        schedule.run_pending()
        time.sleep(0.5)


if __name__ == '__main__':
    cron_thread = Thread(target=runJobs)
    cron_thread.start()
    schedule.every(1).seconds.do(send_status_if_round_time)
    port = 5000 if not(len(sys.argv)>1) else int(sys.argv[1])
    app.run(port=port)
    app.run()
