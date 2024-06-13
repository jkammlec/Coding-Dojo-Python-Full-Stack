from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)

app.secret_key = "la llave del destino"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=['post'])
def registro():
    session["usuario"] = request.form["nombre"]
    session["lugar"] = request.form["lugar"]
    session["numero"] = request.form["nro"]
    session["comida"] = request.form["com"]
    return redirect("/futuro")

@app.route("/futuro")
def futuro():
    if "usuario" not in session:
        return redirect("/")
    return render_template("futuro.html")

@app.route("/volver")
def volver():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)