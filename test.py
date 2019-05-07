from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

import httpantry as requests
import requests as req
import json

app = Flask(__name__)
api = Api(app)

CORS(app)

proxy_urls = {
  'http': 'http://localhost:5000'
}

@app.route("/")
def hello():
    r = req.get('http://httpbin.org/ip', proxies=proxy_urls)
    print(r.text)
    return r.text

if __name__ == '__main__':
   app.run(port=5002)