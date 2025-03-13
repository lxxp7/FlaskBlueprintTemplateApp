"""
Frontend 1.0 Example - Routes/Views.

This is a placeholder/example of routes/views for our api blueprint.
All our Views comes here or could be seperated into several files

"""
from FlaskBlueprintTemplateFrontend.utils import forms
from FlaskBlueprintTemplateFrontend.utils.utils import *
from FlaskBlueprintTemplateFrontend.utils.extensions import (
    Blueprint,
    render_template
)

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def home():
    """
    Renders the home page.

    Returns:
        Response: Rendered 'index.html' template.
    """
    return render_template('index.html')


@routes_bp.route("/get_projects", methods=['GET'])
def get_projects():
    return send_request('get_projects', "GET", {})


@routes_bp.route("/insert_project", methods=["GET", "POST"])
def insert_project():
    form = forms.ProjectForm()

    if request.method == "GET":
        return render_template("projects_form.html", form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            params = {
                "project_name" : form.PROJECT_NAME.data,
                "excluded" : form.EXCLUDED.data
            }
        return_value = send_request("ins_projects", "POST", params)
        return return_value