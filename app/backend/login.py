from datetime import datetime, timedelta
from flask import Blueprint, url_for, render_template, redirect, request, session, make_response
from flask_login import login_user
from werkzeug.security import check_password_hash
from app.models import Users

login = Blueprint('login',
                  __name__,
                  template_folder='../frontend/login',
                  static_folder='../frontend/login')

@login.route('/login', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            # Set sesi menjadi permanent
            session['user_id'] = user.id
            session.permanent = True

            # Waktu kedaluwarsa sesi
            session_expiry = datetime.now() + timedelta(minutes=30)

            # Mencetak waktu sesi aktif dan waktu kedaluwarsa
            print(f"Session started at: {datetime.now()}")  # Waktu saat sesi dimulai
            print(f"Session expires at: {session_expiry}")  # Waktu kedaluwarsa sesi

            login_user(user)
            return redirect(url_for('home.show'))
        else:
            error = 'incorrect-password' if user else 'user-not-found'
            return redirect(url_for('login.show') + f'?error={error}')
    
    return render_template('login/login.html')
