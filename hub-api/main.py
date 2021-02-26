
import flask, sys , os , requests, time, json
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
    data = wait_for_authz(code)
    if "access_token" not in data:
        return data
    token = data["access_token"]
    headers = {
        'content-type': "text/plain",
        'authorization': "Bearer {token}".format(token=token)
    }
    # univ = requests.get("http://localhost:8088/server/France/Paris",headers=headers).json()
    # location = requests.get("http://localhost:8080/server/fr/75015",headers=headers).json()
    dog = requests.get("http://localhost:8088/dog",headers=headers)
    cat = requests.get("http://localhost:8080/cat",headers=headers)
    print("Debuuug:")
    print(dog.text)
    print(cat.text)
    # return "<p> Location : {location} </p><br><p> {univ} </p>".format(univ=json.dumps(univ),location=json.dumps(location))
    return "<p> CAT :<br> <img src='{cat}' alt='Cat' width=300' height='300'></p> \
            <br><p> DOG:<br> <img src='{dog}' alt='Cat' width='300' height='300'></p>".format(cat=cat.text,dog=dog.text)


@app.route('/', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
def home():
    return "<h2>Welcome to HUB API</h2>"

app.run(port=8083)