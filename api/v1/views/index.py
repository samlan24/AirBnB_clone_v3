#!/usr/bin/python3

"""
index module
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """Returns status"""
    response = {"status": "OK"}
    return jsonify(response)
