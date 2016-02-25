from app import db
from sqlalchemy_utils import PasswordType


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']))
    token = db.Column(db.String(512))
    token_expiration = db.Column(db.DateTime)

    def __init__(self, email, password, token, token_expiration):
        self.email = email
        self.password = password
        self.token = token
        self.token_expiration = token_expiration

    def __repr__(self):
        return '<id {}>'.format(self.id)
