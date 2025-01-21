from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, request, session, url_for
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
        login_value = request.form['username']  # Can be username, phone, or email
        password = request.form['password']

        # Check if the login value is an email or phone number and adjust the query accordingly
        user = None
        if "@" in login_value:  # Email login
            user = Users.query.filter_by(email=login_value).first()
        elif login_value.isdigit():  # Phone number login (assuming numeric values only)
            user = Users.query.filter_by(phone=login_value).first()
        else:  # Username login
            user = Users.query.filter_by(username=login_value).first()

        if user and check_password_hash(user.password_hash, password):
            # Set session as permanent
            session['user_id'] = user.id
            session.permanent = True

            # Set session expiry time
            session_expiry = datetime.now() + timedelta(minutes=180)
            session['session_expiry'] = session_expiry.strftime('%Y-%m-%d %H:%M:%S')

            # Log session start and expiry times for debugging
            #print(f"Session started at: {datetime.now()}")
            #print(f"Session expires at: {session_expiry}")
            #print(f"Session data: {session}")  # Print entire session
            #print(f"Cookies: {request.cookies}")  # Print cookies

            login_user(user)
            return redirect(url_for('home.show'))
        else:
            error = 'incorrect-password' if user else 'user-not-found'
            return redirect(url_for('login.show') + f'?error={error}')
    
    return render_template('login/login.html')
