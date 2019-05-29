from flask import Blueprint     #Blueprint on authentication of our app request

auth = Blueprint('auth',__name__)

from . import views,forms
