# Flask API wrapper for the checkin process
# Logging and config imports
from logging import getLogger, DEBUG
from config import Config

# External packages
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# App components
from api.flights import FlightsApi

# Initialize logging for this module
logger = getLogger(__name__)

app = Flask("southwest-checkin")
logger.info(f"Flask app {app.name} initialized.")

app.config.from_object(Config)
logger.info("Config applied successfully.")

# Enable CORS for the app to ensure our UI can call the backend API
getLogger('flask_cors').level = DEBUG
CORS(app, resources={r"/api/*": {"origins": Config.WHITELISTED_ORIGINS}})
logger.info("CORS initialized.")

api = Api(app)
logger.info("Flask-RESTful API initialized.")

# Define the functional endpoints
api.add_resource(FlightsApi, "/api/v1/flights")
