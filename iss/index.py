from flask import Flask, jsonify, request
from pyorbital

app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000},
    {'description': 'salary', 'amount': 50410},
    {'description': 'salary', 'amount': 1351350}
]


@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)