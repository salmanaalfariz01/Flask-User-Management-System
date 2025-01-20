from flask import Blueprint, redirect, url_for, session, make_response, flash
from flask_login import LoginManager, login_required, logout_user

logout = Blueprint('logout', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(logout)

@logout.route('/logout')
@login_required
def show():
    logout_user()
    # Hapus data dari session
    session.pop('user_id', None)
    session.pop('username', None)
    # Hapus cookie
    response = make_response(redirect(url_for('login.show') + '?success=logged-out'))
    response.delete_cookie('username')
    return response

@logout.route('/logout', endpoint='logout')  # Menetapkan nama endpoint 'logout'
def show():
    logout_user()  # Logout user
    session.clear()  # Clear session data
    return redirect(url_for('login.show'))  # Redirect ke halaman login
