from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "llave del tesoro"

@app.route("/")
def index():
    #la primera vez que entro
    if "contador" not in session: #si no existe, contador es 0
        session["contador"] = 0 #variable para mostrar visitas
    else:
        session["contador"] += 1 #ya existe, se suma 1

    return render_template("index.html")

@app.route("/destruir_sesion")
def destruir_sesion():
    session.clear()
    return redirect("/")

@app.route("/visitar_2")
def visitar_2():
    session["contador"] += 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)