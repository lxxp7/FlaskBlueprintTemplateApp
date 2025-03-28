"""
Service Main Application.
Describe here what your service is doing.

This file contains functions to initialize Flask and Database.
You shouldn't have to change those functions except for advance functionality.

"""
from FlaskBlueprintTemplateApp.utils.extensions import (
    Flask,
    SQLAlchemy,
    os
)

db = SQLAlchemy()

from FlaskBlueprintTemplateApp.blueprints import register_blueprints

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

    # Chemin absolu vers le répertoire de base de l'application
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Configuration de l'URI de la base de données SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')

    #: Load Flask Configuration
    #:
    #: By Default the application will load `config/settings.py`.
    #: For testing or dev purposes, you can pass a python configuration
    #: file path as parameter of this function.
    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
       app.config.from_object('FlaskBlueprintTemplateApp.config.settings-dev')

    #: Testing mode
    #:
    #: Flask changes some internal behavior so it's easier to test, and other
    #: extensions can also use the flag to make testing them easier.
    if testing is True:
        app.config["TESTING"] = True

    #Init database
    db.init_app(app)

    #import models module to create the tables in the database if the file doesn't exist
    import FlaskBlueprintTemplateApp.models
    with app.app_context():
        db.create_all()  # Make sure this call is done when in app_context

    #: Register Blueprints
    #:
    #: Every Blueprints to load must be added to the following function
    #: being at blueprints/__init__.py
    register_blueprints(app)

    # Root route for the main page at http://host:port/
    @app.route('/')
    def home():
        return "Welcome to the FlaskBlueprintTemplateAPP API! Use the url with '/api/version/route' ex : /api/1.0/"

    return app
