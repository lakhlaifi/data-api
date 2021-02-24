import flask,requests

app = flask.Flask(__name__)

Api = "http://api.zippopotam.us/fr/72000"

def data():
    response = requests.get(Api)
    return response.json()

@app.route('/', methods=['GET'])
def home():
    return data()

app.run(port=8080)