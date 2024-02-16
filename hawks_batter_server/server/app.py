""" App initialization module."""

import logging
from logging.config import dictConfig
from os import path
import yaml
import os
from flask import Flask
from flask_cors import CORS

from .managers.videos_list_manager import videos_list_manager_service
from .managers.video_manager import video_manager_service
from .managers.sensors_manager import sensors_manager_service
from .managers.machine_manager import machine_manager_service
from .extension import api
from .common import HawksProbatterException, handle_server_box_exception
from .rest_api.configuration_controler import bp as configuration_controler_bp
from .rest_api.machine_controler import bp as machine_controler_bp
from .rest_api.shutdown_controler import bp as shutdown_controler


logger = logging.getLogger(__name__)


def create_app(
    config_dir: str = path.join(path.dirname(path.abspath(__file__)), "config"),
):
    """Create the Flask app"""

    # Create app Flask
    app = Flask("Server Pro Batter Hawks")
    cors = CORS(app)

    
    if os.environ['ENV'] == 'prod':
        config = "general-config.yml"
    else:
        config = "general-config-dev.yml"
    print(f"CONFIG FILE: {config}")

    # Get configuration files
    app_config = path.join(config_dir, config)
    logging_config = path.join(config_dir, "logging-config.yml")

    # Load logging configuration and configure flask application logger
    with open(logging_config) as stream:
        dictConfig(yaml.full_load(stream))

    logger.info("App config file: %s", app_config)

    # Load configuration
    app.config.from_file(app_config, load=yaml.full_load)

    # Register extensions
    register_extensions(app)
    # Register blueprints for REST API
    register_blueprints(app)
    logger.info("App ready!!")
    return app


def register_extensions(app: Flask):
    """Initialize all extensions"""

    # Initialize REST APIs.
    #
    # The spec_kwargs dict is used to generate the OpenAPI document that describes our APIs.
    # The securitySchemes field defines the security scheme used to protect our APIs.
    #   - BasicAuth  allows to authenticate a user with a login and a password.
    #   - BearerAuth allows to authenticate a user using a token (the /login API allows to a user
    #     to retrieve a valid token).

    api.init_app(
        app,
        spec_kwargs={
            "info": {"description": "`Server Probater Hawks` OpenAPI 3.0 specification."},
            "components": {
                "securitySchemes": {
                    "basicAuth": {"type": "http", "scheme": "basic"},
                    "tokenAuth": {"type": "http", "scheme": "bearer"},
                },
            },
        },
    )

    # Video list manager extension
    videos_list_manager_service.init_app(app=app)
    # Video manager extension
    video_manager_service.init_app(app=app)    
    # Sensors manager extension
    sensors_manager_service.init_app(app=app)
    # Machine manager extension
    machine_manager_service.init_app(app=app)


def register_blueprints(app: Flask):
    """Store App APIs blueprints."""
    # Register error handler
    app.register_error_handler(HawksProbatterException, handle_server_box_exception)
    # Register REST blueprints
    api.register_blueprint(configuration_controler_bp)
    api.register_blueprint(machine_controler_bp)
    api.register_blueprint(shutdown_controler)