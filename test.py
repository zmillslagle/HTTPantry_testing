from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api

import httpantry as requests

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
    url = "http://www.cielaustral.com/galerie/photo95f.jpg"
    response = requests.get(url)
    print(response.status_code)
    return response.content

if __name__ == '__main__':
   app.run(port=5002)