from flask import Blueprint, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash
from app.models import db, Users, Divisions, Positions  # Mengimpor db dan model
from datetime import datetime  # Tambahkan ini untuk waktu sekarang
import os

register = Blueprint(
    'register',
    __name__,
    static_folder=os.path.abspath('app/frontend/register'),
    template_folder=os.path.abspath('app/frontend/register')
)

@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
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
                    # Gunakan waktu sekarang jika tidak disediakan
                    new_user = Users(
                        username=username,
                        email=email,
                        phone=phone,
                        created_at=datetime.now(),  # Waktu sekarang
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
    positions = Positions.query.filter_by(division_id=division_id).all()
    return {
        'positions': [{'id': p.id, 'name': p.name} for p in positions]
    }
