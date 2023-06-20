from flask import Flask, jsonify
from views.auth import auth
from views.home import home

app = Flask(__name__)
app.secret_key = "hacknitt"


app.register_blueprint(auth, url_prefix="/api/auth") #routes for auth
app.register_blueprint(home, url_prefix="/api/home") #routes for home


@app.route('/api/test', methods=["GET"]) #This is a test route
def test():
    return jsonify({"data" : "Hello, from Backend"})


if __name__ == "__main__":
    app.run(debug=True)