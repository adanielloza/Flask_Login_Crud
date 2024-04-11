# Flask_Login_Crud
Flask application with Login
Description: Crear un login y proteger las rutas(si el usuario ingresa a una ruta y no está autenticado que lo redirija al login)
Table of Contents:
Login

<img width="395" alt="image" src="https://github.com/adanielloza/Flask_Login_Crud/assets/123408012/d50a943d-d651-49c4-88ae-51659551e769">

CRUD

<img width="1503" alt="image" src="https://github.com/adanielloza/Flask_Login_Crud/assets/123408012/6c0556dd-52b8-43f2-adf3-a7d3d6d5d440">

How to Install and Run the Project:

Flask-Login
Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.

- It will:
    Store the active user’s ID in the Flask Session, and let you easily log them in and out.
    Let you restrict views to logged-in (or logged-out) users. (login_required)
    Handle the normally-tricky “remember me” functionality.
    Help protect your users’ sessions from being stolen by cookie thieves.

- However, it does not:
    Impose a particular database or other storage method on you. You are entirely in charge of how the user is loaded.
    Restrict you to using usernames and passwords, OpenIDs, or any other method of authenticating.
    Handle permissions beyond “logged in or not.”
    Handle user registration or account recovery.

Installation
Install the extension with pip:
$ pip install flask-login

How to Use the Project
The most important part of an application that uses Flask-Login is the LoginManager class.
from flask_login import LoginManager
login_manager = LoginManager()
The login manager contains the code that lets your application and Flask-Login work together, such as how to load a user from an ID, where to send users when they need to log in, and the like.

How it Works
You will need to provide a user_loader callback. This callback is used to reload the user object from the user ID stored in the session. It should take the str ID of a user, and return the corresponding user object. For example:

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
It should return None (not raise an exception) if the ID is not valid. (In that case, the ID will manually be removed from the session and processing will continue.)

Application Tests


<img width="1312" alt="image" src="https://github.com/adanielloza/Flask_Login_Crud/assets/123408012/b37cd7f1-fd5d-4ea6-8d92-19f7d90b5f80">

<img width="1295" alt="image" src="https://github.com/adanielloza/Flask_Login_Crud/assets/123408012/f7c9f0d3-9a69-40c1-a834-38d93272b1ea">

<img width="1053" alt="image" src="https://github.com/adanielloza/Flask_Login_Crud/assets/123408012/eb0a7f38-3c20-45f2-94a9-699d959d64ef">

