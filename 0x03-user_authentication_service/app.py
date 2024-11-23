#!/usr/bin/env python3
from flask import Flask, abort, jsonify, request
from auth import Auth


auth = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    """Dummy function"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register():
    try:
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        abort(400)

    try:
        user = auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": user.email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
