from flask import Blueprint, jsonify

home = Blueprint('home', __name__)


@home.route('/getDetails')
def hello():
    return jsonify({"data" : "InProgress"})


@home.route('/modifyDetails')
def hellos():
    return jsonify(({"data":  "InProgress"}))