#!/usr/bin/env python

import os
import sys
from x10_controller import x10_controller
from flask import Flask
from flask import abort, request, jsonify, g
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

heyu_path = os.environ.get("HEYU_PATH")
if heyu_path is None:
    print("Set environment variable HEYU_PATH")
    sys.exit(1)


@app.route('/<string:house_code>/<string:device_number>/', methods=['DELETE', 'POST', 'OPTIONS'])
def heyu_on_off(house_code, device_number):

    results = ""

    x10 = x10_controller(heyu_path)
    if request.method == "POST":
        results = x10.turn_on(house_code, device_number)

    if request.method == "DELETE":
        results = x10.turn_off(house_code, device_number)

    return jsonify(
        results=results,
        house_code=house_code,
        device_number=device_number,
        method=request.method)


@app.route('/<string:house_code>', methods=['DELETE', 'OPTIONS'])
def heyu_all_off(house_code):

    results = ""

    x10 = x10_controller(heyu_path)
    if request.method == "DELETE":
        results = x10.all_off(house_code)

    return jsonify(
        results=results,
        house_code=house_code,
        method=request.method)


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error="Method not allowed"), 405


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404


if __name__ == '__main__':
    app.run()
