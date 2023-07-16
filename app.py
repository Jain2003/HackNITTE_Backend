from flask import Flask, jsonify, session,request
from views.auth import auth
from views.home import home
from views.admin import admin
from views.nativeContest import nativeContest
from sqlOperations import createTables,get_announcement
from apis import get_contests

app = Flask(__name__)
app.secret_key = "hacknitt"

createTables()

app.register_blueprint(auth, url_prefix="/api/auth") #routes for auth
app.register_blueprint(home, url_prefix="/api/home") #routes for home
app.register_blueprint(admin, url_prefix="/api/admin") #routes for admin
app.register_blueprint(nativeContest, url_prefix="/api/nativeContest") #routes for admin


@app.route('/api/test', methods=["GET"]) #This is a test route
def test():
    return jsonify({"data" : "Hello, from Backend"})


@app.route('/api/getContests')
def getContests():
    return jsonify({"data": get_contests()})

@app.route('/api/announcement')
def getAnnouncement():
    announce = get_announcement()
    return jsonify({'data' : announce})

if __name__ == "__main__":
    app.run(debug=True)