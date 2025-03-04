"""
Extensions registry.

All extensions here are used as singletons and initialized in
application factory.
"""
import urllib
import requests
import re
import logging
import ast

from flask import (
    Flask,
    Blueprint,
    request,
    current_app,
    render_template,
    jsonify,
    flash,
)

from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    ValidationError,
    IPAddress
)

from flask_wtf import FlaskForm

