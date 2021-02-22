from wtforms import StringField, PasswordField, DateField, TimeField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm


from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()], description = "Please enter your full name.")
    email = StringField("Email", validators=[DataRequired(), Email()], description = "Please enter your e-mail address.")
    subject = StringField("Subject", validators = [DataRequired()], description = "Please enter the subject of your message.")
    message = TextAreaField("Message", validators = [DataRequired()], description = "Please enter the message you would like to send.")
    send = SubmitField("Send!")
    