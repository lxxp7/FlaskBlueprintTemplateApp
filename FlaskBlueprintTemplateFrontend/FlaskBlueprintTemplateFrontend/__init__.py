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
    Create Flask App.

    Flask Application Factory Pattern. Creating the Flask App in a function
    makes instancing of the app possible for testing or multi-configuration.
    create_app() is recognized by the `flask run` command.

    documentation :
    https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/#basic-factories

    :param config_filename: path to the config file name. If None, default
                            `config/settings.py` is loaded
    :type config_filename: str
    :param testing: unittest mode
    :type testing: bool
    :return: Flask App object
    :rtype: Flask
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
        app.config.from_object('FlaskBlueprintTemplateFrontend.config.settings')

    #: Testing mode
    #:
    #: Flask changes some internal behavior so it's easier to test, and other
    #: extensions can also use the flag to make testing them easier.
    if testing is True:
        app.config["TESTING"] = True


    #: Register Blueprints
    #:
    #: Every Blueprints to load must be added to the following function
    #: being at blueprints/__init__.py
    from FlaskBlueprintTemplateFrontend.routes import register_blueprints
    register_blueprints(app)

    from FlaskBlueprintTemplateFrontend.routes.versions.routes_1_0.routes import home
    # Root route for the main page
    @app.route('/')
    def index():
        return home()

    return app
