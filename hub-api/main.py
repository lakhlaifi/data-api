
import flask, sys , os , requests, time
from flask import Flask,redirect,render_template
from auth import device, wait_for_authz
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True

device_code = ""
@app.route('/register', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
def register():
    html, dev = device()
    device_code = dev
    print(device_code)
    return html

@app.route('/pull/<code>', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
def pull(code):
    token = wait_for_authz(code)
    # if token["access_token"] = "":
    #     return "Invalid Request"
    token = token["access_token"]
    print("token %s", token)
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer {token}".format(token=token)
    }
    print(token["access_token"])
    univ = requests.get("http://localhost:8088/server/France/Paris",headers=headers)
    return json.dumps(univ)


@app.route('/', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
def home():
    return "<h2>Welcome to HUB API</h2>"

app.run(port=8083)