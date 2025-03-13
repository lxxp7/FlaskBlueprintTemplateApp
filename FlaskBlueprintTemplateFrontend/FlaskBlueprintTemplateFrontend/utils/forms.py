from FlaskBlueprintTemplateFrontend.utils.extensions import(
    FlaskForm,
    StringField,
    PasswordField,
    SubmitField,
    DataRequired,
    ValidationError,
    Email,
    EqualTo,
    Length,
    re,
    IPAddress
)
from wtforms import BooleanField


class ProjectForm(FlaskForm):
    """
    Form for setting Unreal Engine paths: Unreal launcher, project, and scripts paths.
    """
    PROJECT_NAME = StringField('Project name', validators=[DataRequired()])
    EXCLUDED = BooleanField('Exclude project')


    submit = SubmitField(label="Insert project")

