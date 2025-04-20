from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_login = SubmitField('Login')
    
    class Meta:
        csrf = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csrf_token.id = 'csrf_token_login'
    
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_register = SubmitField('Register')
    
    class Meta:
        csrf = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csrf_token.id = 'csrf_token_register'