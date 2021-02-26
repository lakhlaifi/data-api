import flask, sys , os , requests, time 
from flask_socketio import SocketIO

data = {}
client_id = "---"
client_secret = "----"
scope = "SCOPE"
grant_type="urn:ietf:params:oauth:grant-type:device_code"
audience= "https://dev-vtnn7u9u.us.auth0.com/api/v2/"
oauth_token_url="https://dev-vtnn7u9u.us.auth0.com/oauth/token"
auth0_url = "https://dev-vtnn7u9u.us.auth0.com/oauth/device/code"

def device():
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data_client = {"client_id": client_id, "scope": scope, "audience": audience}
    res = requests.post(auth0_url, data=data_client,headers=headers)
    data = res.json()
    device_code = data["device_code"]
    verif = '<h2> Welcome to Weather Device </h2> \
        Please Go to : <a href="{verification_uri}">{verification_uri_complete}</a> <br> and insert: <b>{user_code}</b><br><br>\
        <a href="/pull/{code}"><type="Button"/>CONFIRM</a>'.format(**data,code=device_code)
    return verif,device_code

def wait_for_authz(device_code):
        time.sleep(2)
        r = requests.post(oauth_token_url, {'client_secret': client_secret, 'device_code': device_code,'client_id': client_id, 'grant_type': grant_type})
        data =r.json()
        if data.get('error'):
            return "<h3> Not Authorized, please request your token first throught /register </h3><br><p> {error} - {last} </p>".format(**data, last=device_code)
        return data