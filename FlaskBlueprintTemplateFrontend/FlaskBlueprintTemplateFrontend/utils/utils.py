

from FlaskBlueprintTemplateFrontend.utils.extensions import(
    requests,
    urllib,
    ast,
    current_app,
    jsonify,
    flash,
    current_app,
    render_template,
    request
)
import urllib.parse


def get_config(key):
    """
    Retrieves a configuration value from Flask's app config.

    Args:
        key (str): The configuration key.

    Returns:
        Any: The configuration value or None if not found.
    """
    return current_app.config.get(key)


def get_base_api_url():
    """
    Constructs the base API URL using app configuration.

    Returns:
        str: The base API URL.
    """
    server_addr = get_config('SERVER_ADDR')
    api_port = get_config('API_PORT')
    api_version = get_config('API_VERSION')

    base_api_url = f"http://{server_addr}:{api_port}/api/{api_version}/"
    return base_api_url


def send_request(route: str, method: str, params: dict={}):
    """
    Sends an HTTP request to the API.

    Args:
        route (str): The API route.
        method (str): HTTP method ('GET', 'POST', or 'DELETE').
        params (dict): Request parameters.

    Returns:
        JSON: The API response or an error message.
    """
    base_api_url = get_base_api_url()
    request_path = base_api_url + route
    print(request_path)
    if method is not None:
        final_method = method.upper()
    else:
        final_method = request.method.upper()

    try:
        if final_method == 'GET':
            # Ajout des paramètres à l'URL pour une requête GET
            if params:
                encoded_params = [f"{key}={urllib.parse.quote_plus(str(value))}" for key, value in params.items()]
                request_path += "?" + "&".join(encoded_params)
            data = requests.get(request_path)

        elif final_method in ['POST', 'DELETE']:
            headers = {'Content-Type': 'application/json'}
            if final_method == 'POST':
                data = requests.post(request_path, json=params, headers=headers)
            else:  # DELETE request
                data = requests.delete(request_path, json=params, headers=headers)

        if not data or not data.content:
            return jsonify({'error': 'No data found'})

        try:
            return data.json()
        except requests.exceptions.JSONDecodeError as e:
            print(f'Error occurred: {e}')
            return jsonify({})

    except requests.exceptions.RequestException as req_err:
        print(f"Error during the request: {req_err}")
        return jsonify({'error': str(req_err)}), 500
    except Exception as e:
        print(f"Unexpected error in send_request: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500


def handle_post_request(form, endpoint, config_keys):
    """
    Handles form validation and sends a POST request to update settings.
    Args:
        form (FlaskForm): The form containing settings data.
        endpoint (str): The API endpoint to send the request to.
        config_keys (list): List of setting keys to retrieve from the form.

    Returns:
        dict: Response from the API request.
    """
    if form.validate_on_submit():
        settings_dict = {key: getattr(form, key).data for key in config_keys}
        response = send_request(endpoint, 'POST', settings_dict)
        if 'error' not in response:
            current_app.config.update(settings_dict)
        flash_success("Settings updated")
        return response
    else:
        flash_form_errors(form)
        return render_template('index.html', form=form)


def populate_form_from_response(form, response):
    """
    Populates a FlaskForm with data from an API response.
    Args:
        form (FlaskForm): The form instance to populate.
        response (dict): The API response containing data.
    Returns:
        FlaskForm: The form populated with data.
    """
    for field_name, field in form._fields.items():
        if field_name in response:
            field.data = response.get(field_name)
    return form


def flash_form_errors(form):
    """
    Affiche les erreurs d'un formulaire Flask en utilisant le système de flash messages.

    Args:
        form (FlaskForm): Le formulaire contenant les erreurs de validation.

    Affiche un message flash de type "error" pour chaque erreur détectée.
    """
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{field}: {error}", "error")


def flash_error(message):
    """
    Affiche un message d'erreur avec le système de flash messages.

    Args:
        message (str): Le message d'erreur à afficher.

    Affiche un message flash de type "error".
    """
    flash(message, "error")


def flash_success(message):
    """
    Affiche un message de succès avec le système de flash messages.

    Args:
        message (str): Le message de succès à afficher.

    Affiche un message flash de type "success".
    """
    flash(message, "success")


def extract_functions_with_metadata(filepath, category="Routes"):
    """
    Parses a Python file to extract function metadata, including:
    - Function name
    - Associated endpoints (if in a Flask route file)
    - Docstrings

    Args:
        filepath (str): Path to the Python file.
        category (str): Category of functions (e.g., "Routes", "Utility Functions").

    Returns:
        list: A list of dictionaries containing function metadata.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        module = ast.parse(f.read())

    functions = []
    for node in module.body:
        if isinstance(node, ast.FunctionDef):
            endpoints = []
            if category == "Routes":  # Only extract route decorators for route files
                for decorator in node.decorator_list:
                    if (isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Attribute) and decorator.func.attr == "route" and decorator.args and isinstance(decorator.args[0], ast.Constant)):
                        endpoints.append(decorator.args[0].value)

            functions.append({
                "name": node.name,
                "category": category,
                "endpoints": endpoints if endpoints else (["No route"] if category == "Routes" else ["Utility function"]),
                "docstring": ast.get_docstring(node) or "No docstring"
            })
    return functions