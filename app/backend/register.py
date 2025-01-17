# app/backend/register.py
from flask import Blueprint, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash
from app.models import db, Users, Divisions, Positions  # Mengimpor db dan model
import os


register = Blueprint(
    'register',
    __name__,
    static_folder=os.path.abspath('app/frontend/register'),  # Full path to your static folder
    template_folder=os.path.abspath('app/frontend/register')  # Full path to your templates
)

@register.route('/register', methods=['GET', 'POST'])
@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')  # Gunakan `.get()` untuk menghindari KeyError
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        status = request.form.get('status')
        division_id = request.form.get('division_id')
        position_id = request.form.get('position_id')

        # Validasi input
        if username and email and phone and password and confirm_password and division_id and position_id:
            if password == confirm_password:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        phone=phone,  # Pastikan field ini ada di model Users
                        password_hash=hashed_password,
                        status=status,
                        division_id=int(division_id),
                        position_id=int(position_id),
                    )
                    db.session.add(new_user)
                    db.session.commit()
                except db.exc.IntegrityError:
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')
                return redirect(url_for('login.show') + '?success=account-created')
            else:
                return redirect(url_for('register.show') + '?error=password-mismatch')
        else:
            return redirect(url_for('register.show') + '?error=missing-fields')
    else:
        divisions = Divisions.query.all()
        positions = Positions.query.all()
        return render_template(
            'register/register.html',
            divisions=divisions,
            positions=positions
        )

@register.route('/positions/<int:division_id>', methods=['GET'])
def get_positions(division_id):
    # Query untuk mendapatkan posisi berdasarkan division_id
    positions = Positions.query.filter_by(division_id=division_id).all()
    # Kembalikan data posisi sebagai JSON
    return {
        'positions': [{'id': p.id, 'name': p.name} for p in positions]
    }
