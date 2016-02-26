"""Simple RESTful API for stateless, token based authentication"""
import os

from flask import Flask
from flask import request
from flask import jsonify
from flask import g

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# flask extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

from models import *


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(email=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@app.route('/')
def api_root():
    return 'Welcome to your basic token based User Authentication API!'


@app.route('/api/user', methods=['GET', 'PATCH', 'DELETE'])
@auth.login_required
def api_user():
    """Main endpoint for user methods.  This requires a valid authentication
    token."""
    if request.method == 'GET':
        return jsonify({
            'name': g.user.name,
            'email': g.user.email
        })

    elif request.method == 'PATCH':
        if not request.json:
            return jsonify({'message': 'Please set your mimetype as application/json'}), 415

        name = request.json.get('name', False)
        password = request.json.get('password', False)

        if name or password:
            user = User.query.filter_by(email=g.user.email).first()
            if name:
                user.name = name
            if password:
                user.password = password
            db.session.commit()
            return jsonify({'message': 'User record updated'}), 200
        else:
            return jsonify({'message': 'Not modified'}), 304

    elif request.method == 'DELETE':
        User.query.filter_by(email=g.user.email).delete()
        db.session.commit()
        return jsonify({'message': 'Your user account has been deleted'}), 200

    else:
        return jsonify({'message': 'Forbidden'}), 403


@app.route('/api/user/register', methods=['POST'])
def register():
    if not request.json:
        return jsonify({'message': 'Please set your mimetype as application/json'}), 415

    email = request.json.get('email', False)
    password = request.json.get('password', False)
    name = request.json.get('name', '')

    if not email:
        return jsonify({'message': 'Email required'}), 400

    elif not password:
        return jsonify({'message': 'Password required'}), 400

    else:
        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists'}), 400

        try:
            user = User(email=email, password=password, name=name)
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': 'User created successfully'}), 201
        except Exception as e:
            return jsonify({'message': 'There was an error',}), 500


@app.route('/api/user/login')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})

if __name__ == '__main__':
    app.run()
