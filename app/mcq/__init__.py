from flask import Blueprint

mcq = Blueprint('mcq', __name__)

from . import routes
