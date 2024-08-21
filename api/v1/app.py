#!/usr/bin/python3

"""
this is the main app
"""


from api.v1.views import app_views
from flask import make_response
from flask import Flask
from flask import make_response
from flask import jsonify
from flask_cors import CORS
from os import getenv
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown(exception):
    """Closes the current session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    handles 404 errors
    """
    return make_response(jsonify({"error": "Not Found"}), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
