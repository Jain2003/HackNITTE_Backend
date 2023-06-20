from flask import Blueprint, jsonify

home = Blueprint('home', __name__)


@home.route('/getDetails')
def getDetails():
    return jsonify({"data" : "InProgress"})


@home.route('/modifyDetails')
def modifyDetails():
    return jsonify(({"data":  "InProgress"}))