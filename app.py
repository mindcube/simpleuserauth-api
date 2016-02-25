"""Simple RESTful API for stateless authentication"""

from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome to your basic token based User Authentication API!'


@app.route('/api/user', methods=['GET', 'PATCH', 'DELETE'])
def api_user():
    """Main endpoint for user methods.  This requires a valid authentication
    token."""
    pass
    if request.method == 'GET':
        # GET returns user name and email if valid auth token provided
        return 'Display user'
    elif request.method == 'PATCH':
        # PATCH updates user name or email address (200/404)
        return 'Update user'
    elif request.method == 'DELETE':
        # DELETE deletes user account
        return 'Delete user'
    else:
        # return 403 (forbidden)
        pass


@app.route('/api/user/register')
def register():
    """POST updates user name or email address"""
    pass


@app.route('/api/user/login')
def login():
    """POST user logs in with username/pw and is provided a token"""
    pass


@app.route('/api/user/logout')
def logout():
    """GET logs out a user (really just destroys auth token)"""
    pass

if __name__ == '__main__':
    app.run()
