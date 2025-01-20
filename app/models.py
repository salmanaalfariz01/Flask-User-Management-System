from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Users table
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime, nullable=False)
    status = db.Column(db.Enum('active', 'inactive', name='user_status_enum'), default='active', nullable=False)
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=True)  # Optional Division FK
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'), nullable=True)  # Optional Position FK

    def set_password(self, password):
        """Hashes the password and stores it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the password matches the stored hash."""
        return check_password_hash(self.password_hash, password)


# Divisions table
class Divisions(db.Model):
    __tablename__ = 'divisions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    # Relationship with Users table
    users = db.relationship('Users', backref='division', lazy=True)
    positions = db.relationship('Positions', backref='division', lazy=True)


# Positions table
class Positions(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=False)

    # Relationship with Users table
    users = db.relationship('Users', backref='position', lazy=True)
