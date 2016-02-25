Simple flask based RESTful API
==============================

This application is a basic RESTful API created with Python, Flask and Postgres that provides stateless user authentication.

You can access and play around with the API at <https://simpleuserauth-api.herokuapp.com/>

Personal note: I've been wanting to explore building a basic API without the help of a REST framework and so used this as an opportunity to do just that.  Flask is an extremely lightweight application framework and it made the most sense to use it.

Architecture
------------

This is an example of a simple, stateless token based user authentication API.  When a user creates an account, once they login they are provided with an authorization token that has a built in expiration date.  The user would then use this token to authenticate against protected resources. Once their token expires they will have to login again.


Local Development
-----------------

To run on your local machine, you need the following prerequisites:

* Postgres server
* Python
* Pip
* Virtualenv

The following enviornment variables must be defined on your local machine:

    export APP_SETTINGS="config.DevelopmentConfig"
    export DATABASE_URL="postgresql://localhost/userauth_api_dev"

Once you are ready, do the following to install:

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

To run the local development server:

    $ python app.py

API Documentation
-----------------

- POST **/api/user/register**

    Registers a new user.

    Requires a JSON object with the following payload:

    ```
    {
        "email": <email address>,
        "password": <password>,
        "name": <name>
    }
    ```
    The _name_ parameter is optional.

    Notes:
    - The password is hashed before it is stored in the database. Once hashed, the original password is discarded.
    - In a production deployment secure HTTP must be used to protect the password in transit.

- GET **/api/user/login**

    Return an authentication token.<br>
    This request must be authenticated using a HTTP Basic Authentication header.<br>
    On success a JSON object is returned with a field `token` set to the authentication token.
    On failure status code 401 (unauthorized) is returned.

    The user would then use this token to authenticate for protected resources.

- GET **/api/user**

    This endpoint returns a json object with the email and name of the authenticated user.<br>
    This request must be authenticated using a HTTP Basic Authentication header. Instead of username and password, the client can provide a valid authentication token in the username field. If using an authentication token the password field is not used and can be set to any value.<br>
    On success a JSON object with data for the authenticated user is returned.<br>
    On failure status code 401 (unauthorized) is returned.

- PATCH **/api/user**

    Updates a user record<br>

    You can use this endpoint to change either the user name or password of the user.  This requires a JSON object with the following payload:

    Requires a JSON object with the following payload:

    ```
    {
        "name": <name>
        "password": <password>,
    }
    ```
    This request must be authenticated using a HTTP Basic Authentication header. Instead of username and password, the client can provide a valid authentication token in the username field. If using an authentication token the password field is not used and can be set to any value.<br>
    On success status code 200 (OK) is returned.<br>
    On failure status code 401 (unauthorized) is returned.

- DELETE **/api/user**

    Deletes the user that is currently authenticated<br>
    This request must be authenticated using a HTTP Basic Authentication header. Instead of username and password, the client can provide a valid authentication token in the username field. If using an authentication token the password field is not used and can be set to any value.<br>
    On success status code 200 (OK) is returned.<br>
    On failure status code 401 (unauthorized) is returned.

