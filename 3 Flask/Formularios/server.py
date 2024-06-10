'''
Importamos Flask (encargado de crear la aplicación)
render_template (renderizar los html)
request (con el cual recibimos la info de formularios)
redirect (redireccionar)
'''
from flask import Flask, render_template,request, redirect

app = Flask(__name__) #Instancia de Flask = Aplicación web

#RUTAS
#Formuluario necesita 3 rutas:
#1- Renderiza/Muestra el formulario
@app.route("/")
def index():
    return render_template("index.html")

#2- Recibe la info del formulario
@app.route("/registrar", methods=['post'])
def registrar():
    print(request.form) #imprime diccionario completo
    print(request.form['email']) #imprime un valor del diccionario
    return redirect("/exito")
'''
request.form = {
    "nombre":"Juana de Arco",
    "email":"email@email.com"
    }
'''
#Renderizar = Mostrar una plantilla html
#NUNCA renderizamos una plantilla cuando recibo un POST
#En su lugar: redirigimos a otra ruta /exito

#3- Ruta a la que redirigimos
@app.route("/exito")
def exito():
    return render_template("exito.html")

if __name__ == "__main__":
    app.run(debug=True)