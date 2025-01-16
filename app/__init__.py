from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Pastikan path ini sesuai dengan lokasi file konfigurasi
from app.config.development import DevelopmentConfig  

db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__, 
                static_folder='../frontend/static', 
                template_folder='../frontend') 
    app.config.from_object(DevelopmentConfig)  # Muat konfigurasi di sini
    
    # Inisialisasi database
    db.init_app(app)

    # Register Blueprints
    from app.backend.index import index
    from app.backend.login import login
    from app.backend.logout import logout
    from app.backend.register import register
    from app.backend.home import home

    app.register_blueprint(index)
    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(register)
    app.register_blueprint(home)

    return app
