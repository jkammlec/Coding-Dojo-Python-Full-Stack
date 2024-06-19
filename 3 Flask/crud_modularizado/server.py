#Importación de flask_app
from flask_app import  app
#Importación controladores
from flask_app.controllers import usuarios_controller
#Ejecución de la app
if __name__ =="__main__":
    app.run(debug=True)