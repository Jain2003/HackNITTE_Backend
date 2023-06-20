from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return jsonify({"data" : "InProgress"})


@auth.route('/register')
def register():
    return jsonify({"data":  "InProgress"})

@auth.route('/isLoggedIn')
def isLoggedIn():
    return jsonify({"data": False})

