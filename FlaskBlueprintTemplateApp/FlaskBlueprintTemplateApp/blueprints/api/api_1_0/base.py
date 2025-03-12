"""
API 1.0 Example - Routes/Views.

This is a placeholder/example of routes/views for our api blueprint.
All our Views comes here or could be seperated into several files

"""
from FlaskBlueprintTemplateApp.utils import utils
import FlaskBlueprintTemplateApp.models as models
from FlaskBlueprintTemplateApp.utils.extensions import (
    os,
    current_app,
    request,
    jsonify
)

#: Importing our API Blueprint
#: All the views will be attached to our blueprint with the @api.route decorator.
from FlaskBlueprintTemplateApp.blueprints.api.api_1_0 import api
from FlaskBlueprintTemplateApp.utils.extensions import db

@api.route('/')
def index():
    """
    Returns the main page of the API.

    This is a placeholder for the root URL.

    Returns:
    str: A simple message indicating the main page.
    """
    return jsonify("Main page")


@api.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == "GET":
        settings = None
        return jsonify(settings)
    else:
        utils.update_settings(request)


@api.route('/get_projects', methods=["GET"])
def get_projects():
    projects = models.Projects.query.all()
    projects_json = [project.to_dict() for project in projects]

    return projects_json


@api.route('/ins_projects', methods=["POST"])
def ins_projects():
    data = request.get_json()
    data_project_name = data.get('project_name')
    data_excluded = data.get('excluded')

    if check_pk_bfr_insert("project_name", data_project_name):
        project = models.Projects(project_name=data_project_name, excluded=data_excluded)
        db.session.add(project)
        db.session.commit()
        return get_projects()
    else:
        return jsonify(f"Error duplicate primary keys for {data_project_name}")


def check_pk_bfr_insert(primary_key, value):
    count = models.Projects.query.filter_by(primary_key=value).count()
    if count!=0:
        return True
    return False


from sqlalchemy.orm import class_mapper
@api.route('/get_pr_pk', methods=["GET"])
def get_pr_pk():
    pks = [pk.name for pk in models.Projects.__table__.primary_key]
    return jsonify(pks)