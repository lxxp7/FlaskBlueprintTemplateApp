"""
Extensions registry.

All extensions here are used as singletons and initialized in
application factory.
"""
import os
import subprocess
import logging
import socket
import uuid
import json
import requests
import time
import tempfile
import shutil

from flask import (
    Flask,
    Blueprint,
    jsonify,
    render_template,
    url_for,
    current_app,
    request,
    flash,
)

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime, timedelta
from urllib.parse import unquote

