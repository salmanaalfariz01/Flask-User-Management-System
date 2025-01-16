from app import create_app, db
from flask_migrate import Migrate

# Inisialisasi aplikasi
app = create_app('development')

# Inisialisasi Flask-Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
