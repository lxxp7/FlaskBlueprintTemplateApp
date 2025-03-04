from .routes import routes_bp  # Import the blueprint
# from .client import client_bp  # Import the blueprint

def register_routes(app):
    """Registers all routes with the Flask app."""
    app.register_blueprint(routes_bp)
    # app.register_blueprint(client_bp)
