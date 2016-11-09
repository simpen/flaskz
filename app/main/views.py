from flask import render_template
from . import main


# from .. import db
# from ..models import User
# from ..email import send_email
# from .forms import NameForm


@main.route('/')
def index():
    return render_template('index.html')
