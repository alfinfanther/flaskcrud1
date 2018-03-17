from app import db

class Users(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(35), index=True, unique=True)
    first_name = db.Column(db.String(35), index=True)
    last_name = db.Column(db.String(35), index=True)
    password_hash = db.Column(db.String(150))