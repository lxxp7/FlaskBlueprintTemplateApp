"""Utils module containing all frquently used functions"""

from FlaskBlueprintTemplateApp.utils.extensions import (
    jsonify,
    current_app,
)

def return_data(data):
    """
    Return a JSON response containing the provided data.

    Args:
        data (dict | list): The data to include in the response.

    Returns:
        Response: A JSON response with a 200 status code.
    """
    return jsonify(data),200


def return_success(message):
    """
    Return a JSON success response.

    Args:
        message (str): The success message.

    Returns:
        Response: A JSON response containing the success message with a 200 status code.
    """
    return jsonify(
        {"success" : message}
    ), 200


def return_error(message, code=400):
    """
    Return a JSON error response.

    Args:
        message (str): The error message.
        code (int, optional): The HTTP status code to return. Defaults to 400.

    Returns:
        Response: A JSON response containing the error message with the specified status code.
    """
    return jsonify(
        {"error" : message}
    ), code


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
            return return_error(f"Missing parameter for {setting_name}")
        else:
            current_app.config.update(
                {setting_name : value}
            )