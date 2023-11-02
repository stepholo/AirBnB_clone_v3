#!/usr/bin/python3
"""Flask app"""

from os import getenv
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS  # Import the CORS class


app = Flask(__name__)
app.register_blueprint(app_views)

# Create a CORS instance for the app
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_storage(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.errorhandler(404)
def handle_error_page(error):
    """JSONify not found error page"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
