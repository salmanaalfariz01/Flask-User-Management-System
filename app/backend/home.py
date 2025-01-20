from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from app.models import db, Users

home = Blueprint('home', __name__, template_folder='../frontend/home', static_folder='../frontend/home')
login_manager = LoginManager()
login_manager.init_app(home)

@home.route('/home', methods=['GET'])
@login_required
def show():
    return render_template('home.html')
