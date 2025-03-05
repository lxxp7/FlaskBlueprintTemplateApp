"""
API 1.0 Example - Routes/Views.

This is a placeholder/example of routes/views for our api blueprint.
All our Views comes here or could be seperated into several files

"""
from FlaskBlueprintTemplateApp.utils import utils

from FlaskBlueprintTemplateApp.utils.extensions import (
    os,
    current_app,
    request,
    jsonify
)

#: Importing our API Blueprint
#: All the views will be attached to our blueprint with the @api.route decorator.
from FlaskBlueprintTemplateApp.blueprints.api.api_1_0 import api

@api.route('/')
def index():
    """
    Returns the main page of the API.

    This is a placeholder for the root URL.

    Returns:
    str: A simple message indicating the main page.
    """
    return jsonify("Main page")


@api.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == "GET":
        settings = None
        return jsonify(settings)
    else:
        utils.update_settings(request)


