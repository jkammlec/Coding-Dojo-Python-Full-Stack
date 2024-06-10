from flask import Flask, render_template

app = Flask(__name__)

# RUTAS
@app.route("/loteria")
def nivel1():
    return render_template("index.html", filas=4)


@app.route("/loteria/<int:filas>")  # /loteria/10
def nivel2(filas):
    return render_template("index.html", filas=filas)


if __name__ == "__main__":
    app.run(debug=True)