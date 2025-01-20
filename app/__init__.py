# app/__init__.py
from flask import Flask, session, flash, redirect, url_for
from app.config.development import DevelopmentConfig 
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from app.models import Users
# Register Blueprints
from app.backend.index import index
from app.backend.login import login
from app.backend.logout import logout
from app.backend.register import register
from app.backend.home import home 
from app.models import db

# Create a LoginManager instance
login_manager = LoginManager()

def create_app(config_name='development'):
    app = Flask(__name__, 
                static_folder='../frontend', 
                template_folder='../frontend')
    app.config.from_object(DevelopmentConfig)  # Muat konfigurasi yang sesuai
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Set the user_loader function
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # Set the login view if needed
    login_manager.login_view = 'login.show'

    @app.before_request
    def check_session_expiry():
        if current_user.is_authenticated:
            if 'user_id' not in session:
                # Logout user jika session habis
                logout_user()
                flash('Session Anda telah habis. Silakan login kembali.', 'warning')
                return redirect(url_for('login.show'))


    

    app.register_blueprint(index)
    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(register)
    app.register_blueprint(home)

    return app
