from flask import render_template
from . import mcq


@mcq.route('/')
def index():
    return 'Welcome'
