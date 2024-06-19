from flask import Flask, render_template,request,redirect
from usuario import Usuario

app = Flask(__name__)

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

if __name__ =="__main__":
    app.run(debug=True)