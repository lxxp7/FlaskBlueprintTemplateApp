"""
API 1.0 Example - Blueprint.

We initialze the Blueprint object of our API here so we can share it in all
submodule.

This will be register into the Flask Application via the register_blueprint().
You have to add your new blueprint in register_blueprint for Flask to load it.
"""
from FlaskBlueprintTemplateFrontend.extensions import Blueprint

#: Initialize Blueprint
#:
#: Blueprint's name must be unique. Consider using the path to the module to
#: avoid name clashing
api = Blueprint('api_1_0', __name__)

#: Import all submodule of this API
#:
#: This is done at the end of the file to avoid cyclic import module as
#: recommended in the Flask documentation :
#: https://tinyurl.com/r9cfm72
#:
#: we use '# noqa: F401' so flake8 doesn't do a warning for the import not
#: being at the top of this file.
from .api_1_0 import base  # noqa: F401

