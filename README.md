# Flask_RESTful_API

Why flask?
 - Easy to get started 😊
 - Great for building Rest APIs and microservices.
 - Used by big companies like Netflix, Reddit, Lyft, Et cetera.
 - Great for building APIS for machine learning applications.
 - Force is strong with this one 😉

Who is this series for?
 - Beginners with basic Python knowledge who wants to build cool apps.
 - Experienced flask developers who have been working with flask `SSR` (Server Side Rendering).

## First of all install `pipenv`
using command

```
pip install --user pipenv
```

`Pipenv` is used to create a `virtual environment` which isolates the python packages you used in this project from other system python packages. So, that you can have a different version of same python packages for different projects.

Now, let's install `flask` using `pipenv`
```
pipenv install flask
```
This will create a new virtual environment and install flask. This command will create two files `Pipfile` and `Pipfile.lock`.

Pipfile contains the packages that are required for your application. As you can see `flask` is added to `[packages]` list. This means when someone downloads your code and runs `pipenv install`, `flask` gets installed in their system. Great, right?

If you are familiar with `requirements.txt`, think `Pipfile` as the `requirements.txt` on steroids.


Flask is so simple that you can create an API using a single file. (But you don't have to 😅)

Create a new file called `app.py` where we are gonna write our Flask Hello World API. Write the following code in `app.py`

REST-auth
=========

Companion application to my [RESTful Authentication with Flask](http://blog.miguelgrinberg.com/post/restful-authentication-with-flask) article.

Installation
------------

After cloning, create a virtual environment and install the requirements. For Linux and Mac users:

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

If you are on Windows, then use the following commands instead:

    $ virtualenv venv
    $ venv\Scripts\activate
    (venv) $ pip install -r requirements.txt

# Running
-------

To run the server use the following command:

    (venv) $ python api.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

Then from a different terminal window you can send requests.

## API Documentation
-----------------

- POST **/api/users**

    Register a new user.<br>
    The body must contain a JSON object that defines `username` and `password` fields.<br>
    On success a status code 201 is returned. The body of the response contains a JSON object with the newly added user. A `Location` header contains the URI of the new user.<br>
    On failure status code 400 (bad request) is returned.<br>
    Notes:
    - The password is hashed before it is stored in the database. Once hashed, the original password is discarded.
    - In a production deployment secure HTTP must be used to protect the password in transit.

- GET **/api/users/&lt;int:id&gt;**

    Return a user.<br>
    On success a status code 200 is returned. The body of the response contains a JSON object with the requested user.<br>
    On failure status code 400 (bad request) is returned.

- GET **/api/token**

    Return an authentication token.<br>
    This request must be authenticated using a HTTP Basic Authentication header.<br>
    On success a JSON object is returned with a field `token` set to the authentication token for the user and a field `duration` set to the (approximate) number of seconds the token is valid.<br>
    On failure status code 401 (unauthorized) is returned.

- GET **/api/resource**

    Return a protected resource.<br>
    This request must be authenticated using a HTTP Basic Authentication header. Instead of username and password, the client can provide a valid authentication token in the username field. If using an authentication token the password field is not used and can be set to any value.<br>
    On success a JSON object with data for the authenticated user is returned.<br>
    On failure status code 401 (unauthorized) is returned.

## Example
-------

The following `curl` command registers a new user with username `miguel` and password `python`:

    $ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"miguel","password":"python"}' http://127.0.0.1:5000/api/users
    HTTP/1.0 201 CREATED
    Content-Type: application/json
    Content-Length: 27
    Location: http://127.0.0.1:5000/api/users/1
    Server: Werkzeug/0.9.4 Python/2.7.3
    
    {
      "username": "miguel"
    }

These credentials can now be used to access protected resources:

    $ curl -u miguel:python -i -X GET http://127.0.0.1:5000/api/resource
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 30
    Server: Werkzeug/0.9.4 Python/2.7.3
    
    {
      "data": "Hello, miguel!"
    }

Using the wrong credentials the request is refused:

    $ curl -u miguel:ruby -i -X GET http://127.0.0.1:5000/api/resource
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: text/html; charset=utf-8
    Content-Length: 19
    WWW-Authenticate: Basic realm="Authentication Required"
    Server: Werkzeug/0.9.4 Python/2.7.3
    
    Unauthorized Access

Finally, to avoid sending username and password with every request an authentication token can be requested:

    $ curl -u miguel:python -i -X GET http://127.0.0.1:5000/api/token
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 139
    Server: Werkzeug/0.9.4 Python/2.7.3
    
    {
      "duration": 600,
      "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc"
    }

And now during the token validity period there is no need to send username and password to authenticate anymore:

    $ curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc:x -i -X GET http://127.0.0.1:5000/api/resource
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 30
    Server: Werkzeug/0.9.4 Python/2.7.3
    
    {
      "data": "Hello, miguel!"
    }

Once the token expires it cannot be used anymore and the client needs to request a new one. Note that in this last example the password is arbitrarily set to `x`, since the password isn't used for token authentication.

An interesting side effect of this implementation is that it is possible to use an unexpired token as authentication to request a new token that extends the expiration time. This effectively allows the client to change from one token to the next and never need to send username and password after the initial token was obtained.
