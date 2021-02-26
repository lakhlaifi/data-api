import flask,requests,operator,json
from flask import jsonify
from flask_cors import CORS, cross_origin
from auth import requires_auth, AuthError
app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

def data(country,state):
    universities = []
    headers = {"country": country}
    Api= "http://universities.hipolabs.com/search"
    response = requests.get(Api,headers=headers)
    data =list(map(operator.itemgetter('name'), response.json()))
    for x in data: 
        if state in x:
            universities.append(x)
    return json.dumps(universities)

@app.route('/server/<country>/<state>', methods=['GET'])
# server?country=France
@requires_auth
@cross_origin(headers=['Content-Type', 'Authorization'])
def server(country,state):
    return data(country,state)

@app.route('/', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
def home():
    return "<h2>Welcome to University API</h2>"

app.run(port=8088)