import backup
import sync
from flask import Flask
import config as conf
import flask
import shutil
import os
app = Flask(__name__)

FILENAME = conf.FILENAME
TMP_FILENAME = f"{FILENAME}.tmp"
FILENAME_URI = f"/{FILENAME}"
TMP_FILENAME_URI = f"/{TMP_FILENAME}"

@app.route(FILENAME_URI, methods=["GET", "DELETE"])
def read_write_file():

    if flask.request.method == "GET":

        if conf.ENABLE_SYNC:
            sync.get_latest()

        return flask.send_file(FILENAME)

    elif flask.request.method == "DELETE":

        backup.make_backup()
        os.remove(FILENAME)
        return "ok"

@app.route(TMP_FILENAME_URI, methods=["PUT", "MOVE"])
def read_write_temporary():

    if flask.request.method == "PUT":

        with open(f"{FILENAME}.tmp", "bw") as f:
            f.write(flask.request.data)

        return "ok"

    elif flask.request.method == "MOVE":

        destination = flask.request.headers.get("Destination")
        destination = destination.split("/")[-1]

        if destination != FILENAME:
            return "unexpected destination header", 400

        shutil.move(TMP_FILENAME, destination)

        if conf.ENABLE_SYNC:
            sync.push_changes()

        return "ok"
