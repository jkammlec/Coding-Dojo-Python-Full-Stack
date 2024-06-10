from flask import Flask, render_template #importa Flask y me permite crear la aplicación web

app = Flask(__name__) #crea una nueva instancia de la clase Flask llamada "app"

@app.route("/") #Decorado @, genera la ruta "/" (raíz) y asociamos con la función inmediata
def inicio():
    return "¡Hola desde Flask!" #Devolver el texto "¡Hola desde Flask!"

@app.route("/hola/<name>")
def hola(name):
    return "Hola "+ name

@app.route("/numero/<int:n>")

@app.route("/numero/<int:n>") #Forzosamente indico que en ese espacio debe ir un entero
def numero(n):
    print(f"El usuario ingresó {n}")
    respuesta = f"Ingresaste el numero {n}"
    return respuesta

@app.route("/bienvenidas")
def bienvenidas():
    return render_template("index.html")

@app.route("/usuarios/<name>/<int:num>")
def usuarios(name,num):
    usuarios = ["Juana de Arco", "Pablo Picasso", "Pedro Páramo"]
    return render_template("usuarios.html", nombre=name, numero=num, usuarios=usuarios)

#Asegura que este archivo que el se está ejecutando directamente en el módulo
if __name__ == "__main__":
    app.run(debug=True) #Ejecuta mi aplicación, en modo depuración

