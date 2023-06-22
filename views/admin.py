from flask import Blueprint, jsonify, request, session
from sqlOperations import authenticate_admin,run_query


admin = Blueprint('admin', __name__)


@admin.route("/login", methods=["POST"])
def login():
    print(session.get("admin"))
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    if username is None or password is None:
        return jsonify({"data": "invalid body", "error": True})
    flag = authenticate_admin(username, password)
    if flag:
        session["admin"] = True
        print(session["admin"])
        return jsonify({"data": "Authenticated", "error" : False})
    else:
        session["admin"] = False
        return jsonify({"data": "Wrong password", "error" : False})


@admin.route("/isAdmin")
def isAdmin():
    print(session.get("admin"))
    if session.get("admin", None):
        return jsonify({"data": True})
    else:
        return jsonify({"data": False})


@admin.route("/query", methods=["POST"])
def execquery():
    data = request.get_json()
    query = data.get("query", None)
    key = data.get("key",None)
    if key is None or query is None:
        return jsonify({"data": "invalid body", "error": True})
    result = run_query(query,key)
    return jsonify({"data" : result})
