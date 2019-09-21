from flask import Flask, jsonify, request, make_response
from parse_data import scrape, parse
from iss import app


@app.route("/")
def tle_data():
    tle_list = scrape()
    data = parse(tle_list)
    return jsonify(data)


@app.errorhandler(404)
def wrong_route(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)
