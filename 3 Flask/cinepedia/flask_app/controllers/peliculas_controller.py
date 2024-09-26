from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.pelicula import Pelicula

@app.route("/nuevo")
def nuevo():
    if 'user_id' not in session:
        return redirect("/")

    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    # Va a recibir el formulario... request.form = diccionario con toda la info del formulario
    # Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")

    if not Pelicula.validate_peli(request.form):
        return redirect("/nuevo")

    Pelicula.create(request.form)
    return redirect("/dashboard")

@app.route("/ver/<int:id>")
def read(id): #id = 1
    if 'user_id' not in session:
        return redirect("/")

    dicc = {"id":id}
    pelicula = Pelicula.read_one(dicc)

    return render_template("view.html", pelicula=pelicula)

@app.route("/borrar/<int:id>")
def delete(id): #id = 1
    if 'user_id' not in session:
        return redirect("/")

    dicc = {"id": id}
    Pelicula.delete(dicc)
    return redirect("/dashboard")

@app.route("/editar/<int:id>")
def edit(id):
    if 'user_id' not in session:
        return redirect("/")

    dicc = {"id":id}
    pelicula = Pelicula.read_one(dicc)

    return render_template("edit.html",pelicula=pelicula)

@app.route("/update", methods=["POST"])
def update():
    if 'user_id' not in session:
        return redirect("/")

    # Validamos
    if not Pelicula.validate_peli(request.form):
        return redirect("/editar/" + request.form["id"])

    Pelicula.update(request.form)
    return redirect("/dashboard")