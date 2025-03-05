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
        update_settings(request)


def update_settings(request):
    """
    Updates the application settings based on JSON data received in the request.

    Returns:
        dict: A success response if settings are updated, or an error response if a
        required parameter is missing.
    """
    data:dict = request.get_json()  # This gets the JSON data from the body of the request
    for setting_name, value in data.items():
        if value is None:
            return utils.return_error(f"Missing parameter for {setting_name}")
        else:
            current_app.config.update(
                {setting_name : value}
            )