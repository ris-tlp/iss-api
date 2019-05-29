from flask import Flask, jsonify, request, make_response
from .tle_scrape import scrape
from .convertdata import parse

app = Flask(__name__)

@app.route("/")
def tle_data():
    tle_list = scrape()
    data = parse(tle_list)
    return jsonify(data)

@app.errorhandler(404)
def wrong_route(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)