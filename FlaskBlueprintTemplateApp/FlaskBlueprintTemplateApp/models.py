from FlaskBlueprintTemplateApp.utils.extensions import db

class Projects(db.Model):
    __tablename__ = 'projects'
    project_name = db.Column(db.String(256), primary_key=True, nullable=False)
    excluded = db.Column(db.Boolean, default=False)

    def to_dict(self): # to get a json format
        return {
            "project_name": self.project_name,
            "excluded": self.excluded,
        }
