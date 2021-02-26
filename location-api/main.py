import flask,requests
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

def data(Api):
    response = requests.get(Api)
    return response.json()

@app.route('/server/<country>/<zipcode>', methods=['GET'])
# server/us/90210
@requires_auth
@cross_origin(headers=['Content-Type', 'Authorization'])
def server(country,zipcode):
    Api= "http://api.zippopotam.us/"+country+"/"+ zipcode
    print(Api)
    return data(Api)

@app.route('/cat', methods=['GET'])
@requires_auth
@cross_origin(headers=['Content-Type', 'Authorization'])
def cat():
    response = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
    return response

@app.route('/', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
def home():
    return "<h2>Welcome to Location API</h2>"

app.run(port=8080)