from flask import Blueprint, render_template, session
from app.models import db, Users, Divisions, Positions

home = Blueprint(
    'home',
    __name__,
    template_folder='../frontend/home',
    static_folder='../frontend/home',
)

@home.route('/home', methods=['GET'])
def show():
    # Inisialisasi user_details sebagai None
    user_details = None

    if 'user_id' in session:
        user_id = session['user_id']

        # Menggunakan SQLAlchemy ORM untuk query data
        user = Users.query.filter_by(id=user_id).first()

        if user:
            # Mendapatkan division dan position menggunakan relasi yang sudah didefinisikan
            division = user.division.name if user.division else 'N/A'
            position = user.position.name if user.position else 'N/A'

            # Simpan hasil ke session
            session['username'] = user.username
            session['division'] = division
            session['position'] = position

            # Set user details
            user_details = {
                'username': user.username,
                'division': division,
                'position': position
            }
        else:
            session['username'] = None
            session['division'] = 'N/A'
            session['position'] = 'N/A'

    return render_template('home/home.html', user_details=user_details)
