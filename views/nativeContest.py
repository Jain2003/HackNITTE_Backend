from flask import Blueprint, jsonify, request
from sqlOperations import get_native_contests,get_native_contest_details
from apis import submit_code

nativeContest = Blueprint('nativeContest', __name__)


@nativeContest.route("/getContests")
def getContests():
    return jsonify({"data": get_native_contests()})


@nativeContest.route("/getContestName")
def getContestName():
    return jsonify({"data" : get_native_contest_details()[0][0] })


@nativeContest.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    code = data["code"]
    lang = data["lang"]
    prob = data["prob"]
    return jsonify({"data" : submit_code(code,lang,prob)})
