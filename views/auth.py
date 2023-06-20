from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)


@auth.route('/login')
def hello():
    return jsonify({"data" : "InProgress"})


@auth.route('/register')
def hellos():
    return jsonify(({"data":  "InProgress"}))

