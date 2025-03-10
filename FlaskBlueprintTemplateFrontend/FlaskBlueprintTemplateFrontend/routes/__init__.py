"""
Blueprints.

Here is the list of all the Blueprints we want to be loaded in the Flask
Application.
https://flask.palletsprojects.com/en/1.1.x/blueprints/

The register_blueprints() is called by the create_app() after Flask got
configured.

"""
#: Import blueprints from submodule
from .versions.routes_1_0.routes import routes_bp  # Import the blueprint

def register_blueprints(app):
    """
    Register Flask Blueprints.

    This function will be called just after the Flask Application got
    initialized.

    :param flask_app: Flask app object
    :type flask_app: Flask
    """
    #: Register the api_1_0 example
    #:
    #: Here you can specify the prefix of the URL.
    #: This is how the 'add' api call will be accessible:
    #: without prefix: http://localhost:8080/add/
    #: with prefix: http://localhost:8080/api/1.0/add
    #: To check your routes, use 'flask routes' in the terminal
    app.register_blueprint(routes_bp, url_prefix="/routes/1.0")
    #: Add your blueprints here...
