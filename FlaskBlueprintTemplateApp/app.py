from FlaskBlueprintTemplateApp import create_app
from flask_cors import CORS

# Create the Flask app instance
app = create_app()

# Enable CORS to allow cross-origin requests
CORS(
    app,
    resources={
        r"/*": {"origins": "*"}  # Allow requests from any origin (use specific domains in production)
    }
)

# Run the app
if __name__ == '__main__':
    app.run()
