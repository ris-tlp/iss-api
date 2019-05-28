from flask import Flask, jsonify, request
from .tle_scrape import scrape
from .convertdata import parse

app = Flask(__name__)

@app.route("/")
def tle_data():
    tle_list = scrape()
    data = parse(tle_list)
    return jsonify(data)

