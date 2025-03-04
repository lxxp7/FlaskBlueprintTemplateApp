"""
Frontend 1.0 Example - Routes/Views.

This is a placeholder/example of routes/views for our api blueprint.
All our Views comes here or could be seperated into several files

"""
from FlaskBlueprintTemplateFrontend.extensions import (
    Blueprint,
    render_template
)

routes_bp = Blueprint('routes', __name__)  # Define the blueprint

@routes_bp.route('/')
def home():
    """
    Renders the home page.

    Returns:
        Response: Rendered 'index.html' template.
    """
    return render_template('index.html')