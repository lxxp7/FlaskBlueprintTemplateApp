"""
Flask Configuration Dev Mode.

This is a Flask Configuration compatible with Celery.
It holds all configuration parameters for the Flask App and the Celery App.
"""
# -----------------------------------------------------------------------------
# Flask Configuration
#
# https://flask.palletsprojects.com/en/1.1.x/config/#builtin-configuration-values
# -----------------------------------------------------------------------------
ENV = "development"
# DEBUG = True
# TEMPLATES_AUTO_RELOAD = True

import os
SECRET_KEY = os.urandom(24)  # Generates a random secret key

SERVER_ADDR = '127.0.0.1'
API_PORT = '5000'
API_VERSION = '1.0'