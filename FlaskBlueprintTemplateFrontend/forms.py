from FlaskBlueprintTemplateFrontend.extensions import(
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

class LoginForm(FlaskForm):
    """
    Form for user login with username, email, and password validation.
    """
    username = StringField(label='username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label='email', validators=[DataRequired(), Email()])
    pwd = PasswordField(label='Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_pwd = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('pwd')])

    submit = SubmitField(label="Login")


class ConfigurationForm(FlaskForm):
    """
    Form for configuring API server settings: address, port, and version.
    """
    SERVER_ADDR = StringField('API Server Address', validators=[DataRequired(), IPAddress()])
    API_PORT = StringField('API Port', validators=[DataRequired()])
    API_VERSION = StringField('API Version', validators=[DataRequired()])
    submit = SubmitField('Save')


def validate_windows_path(form, field):
    """
    Custom validator to ensure the path starts with a disk (e.g., C:/ or D:/).
    """
    path = field.data
    if not re.match(r'^[A-Za-z]:/', path):
        raise ValidationError('Path must start with a valid disk (e.g., C:/).')

class SettingsForm(FlaskForm):
    """
    Form for setting Unreal Engine paths: Unreal launcher, project, and scripts paths.
    """
    Setting1 = StringField('Setting1', validators=[DataRequired()])
    Setting2 = StringField('Setting2', validators=[DataRequired()])
    Setting3 = StringField('Setting3', validators=[DataRequired()])
    Setting4 = StringField('Setting4', validators=[DataRequired()])

