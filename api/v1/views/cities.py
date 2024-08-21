#!/usr/bin/python3
""" New view for City objects that handles
all default RestFul API actions
"""


from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=["GET"], strict_slashes=False)
def city_get_all(state_id):
    """ Retrieves the list of all City objects of a State """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    cities = [city.to_json() for city in state.cities]
    return jsonify(cities)


@app_views.route("/cities/<city_id>", methods=["GET"], strict_slashes=False)
def city_get(city_id):
    """ Retrieves a City object """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_json())


@app_views.route("/cities/<city_id>", methods=["DELETE"], strict_slashes=False)
def city_delete(city_id):
    """ Deletes a City object """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities", methods=["POST"], strict_slashes=False)
def city_create(state_id):
    """ Creates a City object """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    city_json = request.get_json(silent=True)
    if city_json is None:
        abort(400, 'Not a JSON')
    if "name" not in city_json:
        abort(400, 'Missing name')
    city_json["state_id"] = state_id
    new_city = City(**city_json)
    new_city.save()
    return jsonify(new_city.to_json()), 201


@app_views.route("/cities/<city_id>", methods=["PUT"], strict_slashes=False)
def city_update(city_id):
    """ Updates a City object """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    city_json = request.get_json(silent=True)
    if city_json is None:
        abort(400, 'Not a JSON')
    for key, value in city_json.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_json()), 200
