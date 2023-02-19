#!/usr/bin/env python3
"""crrating a basic flask app"""


from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', method=["GET"], strict_slashes=False)
def payload() -> str:
    """return payload jsonify"""
    return jsonify {"message": "Bienvenue"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")