from FlaskBlueprintTemplateApp.utils.extensions import db
"""
models.py

This module defines the database models for the Flask application.
It contains SQLAlchemy models representing database tables.

Classes:
    - Projects: Represents a project with a name and an exclusion flag.
"""

class Projects(db.Model):
    """
    Represents a project in the database.

    Attributes:
        project_name (str): The unique name of the project (Primary Key).
        excluded (bool): A flag indicating whether the project is excluded (default: False).
    """

    __tablename__ = 'projects'

    project_name = db.Column(db.String(256), primary_key=True, nullable=False)
    excluded = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """
        Converts the Project instance into a dictionary format.

        Returns:
            dict: A dictionary containing project details.
        """
        return {
            "project_name": self.project_name,
            "excluded": self.excluded,
        }
