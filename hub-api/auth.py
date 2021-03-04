import flask, sys , os , requests, time 
from flask import render_template

data = {}
client_id = "xxx"
client_secret = "xxxx"
scope = "SCOPE"
grant_type="urn:ietf:params:oauth:grant-type:device_code"
audience= "location-api"
oauth_token_url="https://dev-h-qf4jut.eu.auth0.com/oauth/token"
auth0_url = "https://dev-h-qf4jut.eu.auth0.com/oauth/device/code"

def device():
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data_client = {"client_id": client_id, "scope": scope, "audience": audience}
    res = requests.post(auth0_url, data=data_client,headers=headers)
    data = res.json()
    device_code = data["device_code"]
    verification_uri_complete= data["verification_uri_complete"]
    verification_uri=data["verification_uri"]
    user_code=data["user_code"]
    verif = '<h2> Welcome to HUB Device </h2> \
        <p> Register with your device_code to get access to our APIs</p>\
        Please Go to : <a href="{verification_uri_complete}">{verification_uri}</a> <br> and insert: <b>{user_code}</b><br><br>\
        <a href="/pull/{code}"><type="Button"/>CONFIRM</a>'.format(**data,code=device_code)
    return render_template("home.html", user_code=user_code,device_code=device_code,verification_uri_complete=verification_uri_complete,verification_uri=verification_uri),device_code

def wait_for_authz(device_code):
        r = requests.post(oauth_token_url, {'client_secret': client_secret, 'device_code': device_code,'client_id': client_id, 'grant_type': grant_type})
        data =r.json()
        if data.get('error'):
            return "<h3> Not Authorized, please request your token first throught /register </h3><br><p> {error} - {last} </p>".format(**data, last=device_code)
        return data