from app import db
from config import Config
from sqlalchemy_utils import PasswordType

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']), nullable=False)

    def verify_password(self, password):
        return password == self.password

    def generate_auth_token(self, expiration=1000*60):
        s = Serializer(Config.SECRET_KEY, expires_in=expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(Config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    def __init__(self, email, password, name=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
