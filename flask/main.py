from flask import Flask, render_template, request
from flask import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    breed = StringField("What Breed are you?")
    submit = SubmitField("Submit")

    
