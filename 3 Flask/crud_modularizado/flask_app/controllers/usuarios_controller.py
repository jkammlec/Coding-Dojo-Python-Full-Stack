#Importaciones
from flask import Flask, render_template, request, redirect, session

#Importar la app
from flask_app import app

#Importar los modelos a utilizar
from flask_app.models.usuario import Usuario

#RUTAS

@app.route("/")
def index():
    usuarios = Usuario.mostrar_usuarios()
    return render_template("index.html", listado_usuarios = usuarios)

@app.route("/nuevo")
def nuevo():
    return render_template("nuevo.html")

@app.route("/crear",methods=["POST"])
def crear():
    Usuario.guardar(request.form)
    return redirect("/")
    #Recibimos lo que el usuario ingresó en form
    #request.form = DICCIONARIO con la info

@app.route("/borrar/<int:id>")
def borrar(id):
    diccionario = {"id":id}
    Usuario.borrar(diccionario)
    return redirect("/")

@app.route("/editar/<int:id>")
def editar(id):
    diccionario = {"id":id}
    usuario = Usuario.mostrar_un_usuario(diccionario)
    return render_template("editar.html", usuario=usuario)

@app.route("/actualizar", methods=['POST'])
def actualizar():
    #Método en usuario que actualice la info de un registro
    return redirect("/")