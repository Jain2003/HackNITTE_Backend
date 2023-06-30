from flask import Blueprint, jsonify,request, session
from scrap import scrap
from sqlOperations import regiter_user,login_user,get_user_details,get_all_user_details
auth = Blueprint('auth', __name__)


@auth.route('/login',methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    res = login_user(username, password)
    print(res)
    if res:
        session['user'] = username
        return jsonify({"data" : "Logged In","res" : True})
    else:
        return jsonify({"data" : "Invalid Creds", "res" : False})


@auth.route('/register', methods=["POST"])
def register():
    data = request.get_json()
    if data["password"] != data["cpassword"]:
        return jsonify({'data' : 'password and confirm password didnt match'})
    rating = scrap(data["codechef"],data["codeforces"],data["leetcode"])
    sqldata = [data["username"],data["email"],data["rollno"],data["password"],data["codechef"],data["codeforces"],data["leetcode"],rating[0],rating[1],rating[2]]
    res = regiter_user(sqldata)
    if res:
        return jsonify({"data":  "registered!"})
    else:
        return jsonify({"data" : "unknown error"})


@auth.route('/isLoggedIn')
def isloggedIn():
    if session.get('user',None):
        return jsonify({"data": True})
    else:
        return jsonify({"data": False})

@auth.route('/getUserDetails')
def getDetails():
    username = session.get('user',None)
    if username is None:
        return jsonify({"data" : "Not logged In", "error" : True })
    details = get_user_details(username)

    return jsonify({"data" : details, "eror" : False})

@auth.route('/getAll')
def getAllDetails():
    user = session.get("user",None)
    if user is None:
        return jsonify({"data" : "error", "error" : True})
    details = get_all_user_details()
    return jsonify({"data" : [details,user], "error" : False})
