from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from werkzeug.security import generate_password_hash
from app.models import db, Users

register = Blueprint('register', __name__, template_folder='../app/frontend/register')

@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if username and email and password and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(password, method='sha256')
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        password_hash=hashed_password,  # Sesuaikan atribut di model
                    )
                    db.session.add(new_user)
                    db.session.commit()
                except sqlalchemy.exc.IntegrityError:
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')

                return redirect(url_for('login.show') + '?success=account-created')
        else:
            return redirect(url_for('register.show') + '?error=missing-fields')
    else:
        return render_template('register/register.html')
