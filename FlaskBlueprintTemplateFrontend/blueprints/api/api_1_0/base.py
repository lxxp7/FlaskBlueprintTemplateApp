"""
API 1.0 Example - Routes/Views.

This is a placeholder/example of routes/views for our api blueprint.
All our Views comes here or could be seperated into several files

"""
from FlaskBlueprintTemplateFrontend import utils

from FlaskBlueprintTemplateFrontend.extensions import (
    os,
    request,
    jsonify
)

#: Importing our API Blueprint
#: All the views will be attached to our blueprint with the @api.route decorator.
from FlaskBlueprintTemplateFrontend.blueprints.api.api_1_0 import api

@api.route('/')
def index():
    """
    Returns the main page of the API.

    This is a placeholder for the root URL.

    Returns:
    str: A simple message indicating the main page.
    """
    return jsonify("Main page")
