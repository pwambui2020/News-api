# from flask import Blueprint
# main = Blueprint ('main', __name__)
# from . import views

# from .main import main as main_blueprint


from flask import Blueprint
main = Blueprint('main', __name__)
from . import views,errors


