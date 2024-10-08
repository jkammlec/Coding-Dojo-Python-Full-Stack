from flask import Flask, render_template, redirect, request, session, flash, jsonify
from flask_app import app

# Importamos los modelos
from flask_app.models.user import User

# Importar BCrypt
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


# Plantilla que muestra formularios
@app.route("/")
def index():
    return render_template("index.html")


# Ruta que recibe el formulario
@app.route("/register", methods=['POST'])
def register():
    # request.form = {"first_name": "Elena", "last_name": "De Troya"....}

    # Validar la info que recibimos
    if not User.validate_user(request.form):
        # No es valida la info, redirecciono al form
        return redirect("/")

    # Hashear contraseña
    pass_hash = bcrypt.generate_password_hash(request.form["password"])

    # Crear un diccionario que simule el form, incluyendo la contraseña hasheada
    form = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pass_hash
    }

    id = User.save(form)  # Recibo el ID del nuevo usuario 1
    session["user_id"] = id
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    # Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")

    dicc = {"id":session['user_id']}
    user = User.get_by_id(dicc)

    return render_template("dashboard.html",user=user)


@app.route("/login", methods=["post"])
def login():
    # request.form = email y contraseña

    # Verifico que el email esté en mi BD
    user = User.get_by_email(request.form)  # Recibo false (si no existe) o recibo un objeto de Usuario

    if not user:  # Si user = False
        # flash("E-mail not found", "login")
        # return redirect("/")
        return jsonify(message="E-mail not found")

    # Si user existe
    if not bcrypt.check_password_hash(user.password, request.form["password"]):  # (password hasheado, pass no hasheado)
        # flash("Password incorrect", "login")
        # return redirect("/")
        return jsonify(message="Password incorrect")

    session["user_id"] = user.id
    # return redirect("/dashboard")
    return jsonify(message="success")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")