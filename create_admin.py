from app import app, db, Admin
from werkzeug.security import generate_password_hash

with app.app_context():

    admin = Admin(
        name="SmartPark Admin",
        email="admin@smartpark.com",
        password=generate_password_hash("admin123")
    )

    db.session.add(admin)
    db.session.commit()

    print("Admin account created successfully!")