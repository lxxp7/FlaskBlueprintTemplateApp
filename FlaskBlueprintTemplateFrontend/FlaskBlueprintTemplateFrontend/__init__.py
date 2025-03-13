"""
Service Main Application.
Describe here what your service is doing.

This file contains both function to initialized Flask and Celery App.
You shouldn't have to change those functions except for advance functionality.

"""
from FlaskBlueprintTemplateFrontend.utils.extensions import Flask
from FlaskBlueprintTemplateFrontend.routes import routes_bp

def create_app(config_filename=None, testing=False):
    """
    Create and configure the Flask application.

    Parameters:
    - config_filename (str): The configuration file to load.
    If None,  defaults to 'config/settings-dev.py'.

    Returns:
    - app (Flask): The configured Flask application instance.
    """
    #: Instanciate a Flask App with the name of the service
    app = Flask(__name__)

    #: Load Flask Configuration
    #:
    #: By Default the application will load `config/settings.py`.
    #: For testing or dev purposes, you can pass a python configuration
    #: file path as parameter of this function.
    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        app.config.from_pyfile('config/settings-dev.py')

    #: Testing mode
    #:
    #: Flask changes some internal behavior so it's easier to test, and other
    #: extensions can also use the flag to make testing them easier.
    if testing is True:
        app.config["TESTING"] = True

    # Register routes

    from  FlaskBlueprintTemplateFrontend.routes import register_routes
    register_routes(app)

    return app
