from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar", methods=['post'])
def registrar():
    #print(request.form)
    #print(request.form['email'])
    session["usuario"] = request.form["nombre"]
    session["correo"] = request.form["email"]
    return redirect("/exito")

@app.route("/exito")
def exito():
    if "usuario" not in session:
        return redirect("/")
    return render_template("exito.html")

@app.route("/logout")
def logout():
    #Cerrar sesión
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)