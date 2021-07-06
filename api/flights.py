# Defines the endpoints for the API
import json
from datetime import datetime
from flask import request
from flask_restful import Resource
from logging import getLogger
logger = getLogger(__name__)


class FlightsApi(Resource):
    """
    Enables programmatic access to the auto-checkin process.
    Endpoint: /api/v1/flights
    """

    def get(self) -> json:
        """Return all dormant checkin requests."""
        logger.debug(f"Request: {request}")

        # TODO: Move the list of pending checking requests to a database
        return {"message": "Success", "data": []}, 200
