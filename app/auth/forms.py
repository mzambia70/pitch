from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError #facilitate user input, render a checkbox in our form 
from wtforms.validators import Required,Email,EqualTo   #email follows a proper email address structure and Equal compare 2 passwrd inmputs
from ..models import User



class RegistrationForm(FlaskForm):    #creating four inputs field
    email = StringField("Your Email Address",validators=[Required(),Email()])
    username = StringField("Enter your username",validators=[Required()])
    password = PasswordField("Password",validators=[Required(),EqualTo('password_confirm',message='Passwords must match')])
    password_confirm = PasswordField('Confirm passwords',validators=[Required()])
    submit = SubmitField("Sign Up")


    def validate_email(self,data_field):  #takes in dta field nd checks db 2 confrm there is no user wiht that email address
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email.')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken.')



class LoginForm(FlaskForm):
    email = StringField("Your Email Address",validators=[Required(),Email()])
    password = PasswordField("Password",validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField("Sign In")