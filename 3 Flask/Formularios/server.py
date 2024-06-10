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

if __name__ == "__main__":
    app.run(debug=True)