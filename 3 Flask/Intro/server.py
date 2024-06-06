from flask import Flask #importa Flask y me permite crear la aplicación web

app = Flask(__name__) #crea una nueva instancia de la clase Flask llamada "app"

@app.route("/") #Decorado @, genera la ruta "/" (raíz) y asociamos con la función inmediata
def inicio():
    return "¡Hola desde Flask!" #Devolver el texto "¡Hola desde Flask!"


#Asegura que este archivo que el se está ejecutando directamente en el módulo
if __name__ == "__main__":
    app.run(debug=True) #Ejecuta mi aplicación, en modo depuración

