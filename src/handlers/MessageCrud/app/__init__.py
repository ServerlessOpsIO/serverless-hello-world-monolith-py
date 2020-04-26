#!/usr/bin/env python
'''Application entry point'''
import os

from flask_lambda import FlaskLambda


def _initialize_blueprints(app) -> None:
    '''Register Flask blueprints'''
    from app.routes.message import message
    app.register_blueprint(message)


def create_app() -> FlaskLambda:
    '''Create an app by initializing components'''
    app = FlaskLambda(__name__)

    _initialize_blueprints(app)

    # Do it!
    return app


