#!/usr/bin/python3

"""
index module
"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """Returns status"""
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    retrieves the number of
    each objects by type
    """
    count = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(count)
