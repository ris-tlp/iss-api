from flask import Flask, jsonify, request
from .nasa_scrape import scrape

app = Flask(__name__)

@app.route("/")
def tle_data():
    return scrape()
