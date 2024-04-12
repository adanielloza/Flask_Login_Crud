# Flask_Login_Crud
Flask application with Login
Description: Crear un login y proteger las rutas(si el usuario ingresa a una ruta y no está autenticado que lo redirija al login)


Diagrama de Login

<img width="764" alt="image" src="https://github.com/adanielloza/Flask_Login_Crud/assets/123408012/327bc097-e93a-4cc8-b27c-91d27386d1d9">

Here’s an overview of the structure of a Flask application that uses Flask-Login for user authentication and PostgreSQL as its database:

App Configuration: The Flask app is configured with the database URI and a secret key for session management.
Database Setup: SQLAlchemy is used to set up the PostgreSQL database. A User model is defined with id, username, and password fields.
Login Manager Setup: Flask-Login’s LoginManager is initialized. It handles the session management for logged in users.
User Loader Callback: A user loader callback function is defined. This tells Flask-Login how to find a specific user from the ID stored in the session.
Login Route: A /login route is defined. If the method is POST, it checks the username and password provided by the user, and if they are valid, it logs the user in and redirects them to the dashboard.
Logout Route: A /logout route is defined. It logs out the user and redirects them to the index page.
Dashboard Route: A /dashboard route is defined. This page can only be accessed by logged in users due to the @login_required decorator.
This is a basic structure and does not include features like user registration, password hashing, error handling, nor MVC. I used this engineering structure design and adapt it into my MVC-CRUD 

Remember to replace 'postgresql://username:password@localhost/dbname' and 'your_secret_key' with your actual database URI and secret key.

Tambien me guie con este Diagrama 


![image](https://github.com/adanielloza/Flask_Login_Crud/assets/123408012/e9bf73db-a0cc-4595-8f2d-27103869a6c5)


diagrama de flujo que describe el proceso de autenticación de un usuario a través de una interfaz web. 

Entrada del usuario: El usuario ingresa sus credenciales (nombre de usuario y contraseña) en la interfaz web.
Verificación de las credenciales: La aplicación verifica las credenciales proporcionadas por el usuario. Si las credenciales son incorrectas, se le pide al usuario que las introduzca de nuevo.
Generación de token: Si las credenciales son correctas, la aplicación genera un token de autenticación.
Envío del token al usuario: La aplicación envía el token al usuario. Este token se almacena en las cookies del navegador del usuario.
Uso del token para las solicitudes futuras: Cuando el usuario realiza solicitudes futuras a la aplicación, el token de autenticación se envía junto con la solicitud. Esto permite a la aplicación verificar la identidad del usuario sin necesidad de que este introduzca sus credenciales de nuevo.
Este diagrama destaca el papel de las cookies y los tokens para garantizar un acceso seguro. 

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
