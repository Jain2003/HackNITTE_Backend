from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/test', methods=["GET"])
def test():
    return jsonify({"data" : "Hello, from Backend"})


if __name__ == "__main__":
    app.run(debug=True)