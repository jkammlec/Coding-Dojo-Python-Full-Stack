#Terminal: pipenv install flask pymysql flask-bcrypt
#importar la app
from flask_app import app
#importar controladores
from flask_app.controllers import users_controller, peliculas_controller
#ejecución app
if __name__ == "__main__":
    app.run(debug=True)