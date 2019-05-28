from flask import Flask, jsonify, request
from .nasa_scrape import scrape
from .convertdata import parse

app = Flask(__name__)

@app.route("/")
def tle_data():
    # x = parse(scrape())
    tle_list = scrape()
    x = parse(tle_list)
    # return f'{x} \n {y}'
    # return scrape()
    return x

