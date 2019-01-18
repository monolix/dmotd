from flask import Flask, abort, jsonify, \
    Response

daemon = Flask(__name__)
daemon.config["MOTD_FILE"] = "/etc/motd"

@daemon.route("/raw", methods=["GET"])
def rawMOTD():
    try:
        with open(daemon.config["MOTD_FILE"], "r") as f:
            contents = f.read()
    except FileNotFoundError:
        return Response("Error: not found.", mimetype="text/plain")

    return Response(contents, mimetype="text/plain")

@daemon.route("/json", methods=["GET"])
def jsonMOTD():
    try:
        with open(daemon.config["MOTD_FILE"], "r") as f:
            contents = f.read()
    except FileNotFoundError:
        return jsonify({
            "ok": False,
            "error-code": 404,
            "error-desc": "Not Found."
        })

    return jsonify({
        "ok": True,
        "result": contents
    })
