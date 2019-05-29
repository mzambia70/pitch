from flask_wtf import FlaskForm #help us create a form class
from wtforms import StringField,TextAreaField,SubmitField,SelectField #help us av a textfield,text area and submit button
from wtforms.validators import  Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title')
    category = SelectField('Pitch Category', choices=[('politics', 'politics'),
                                                      ('business', 'business'),
                                                      ('sports', 'sports'),
                                                      ('meme', 'meme'),
                                                      ('art', 'art')])
    content = TextAreaField('Type Here')
    submit = SubmitField('Create Pitch')


class CommentForm(FlaskForm):

    title = StringField('Comment Title')
    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')