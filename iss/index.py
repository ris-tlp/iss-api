from flask import Flask, jsonify, request, make_response
from parse_data import scrape, parse
from iss import app


@app.route("/")
def tle_data():
    tle = scrape()
    coordinates = parse(tle)
    return jsonify(coordinates)


@app.errorhandler(404)
def wrong_route(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)
