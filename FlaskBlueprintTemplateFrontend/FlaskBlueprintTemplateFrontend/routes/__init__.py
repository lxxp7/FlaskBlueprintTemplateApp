from .routes import routes_bp  # Import the blueprint

def register_routes(app):
    """Registers all routes with the Flask app."""
    app.register_blueprint(routes_bp)
