from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms import ValidationError
from dbengines.dbcurrent import db

class CreateKitchen(Form):
    name = StringField('name', [validators.Length(min=4),
        validators.Length(max=20)])

