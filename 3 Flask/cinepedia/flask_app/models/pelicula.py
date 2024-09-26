from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Pelicula:

    def __init__(self,data):
        #data = {diccionario con la info de la bd}
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.director = data["director"]
        self.fecha = data["fecha"]
        self.sinopsis = data["sinopsis"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        self.user_name = data["user_name"] #columna extra al hacer una consulta join

    @classmethod
    def create(cls,form):
        query = "INSERT INTO peliculas (nombre, director, fecha, sinopsis, user_id) VALUES (%(nombre)s,%(director)s,%(fecha)s,%(sinopsis)s,%(user_id)s)"
        return connectToMySQL("cinepedia").query_db(query, form)

    @classmethod
    def read_one(cls,data):
        #data = {"id":1}
        query = "SELECT peliculas.*, users.first_name as user_name FROM peliculas JOIN users ON peliculas.user_id = users.id WHERE peliculas.id = %(id)s;"
        result = connectToMySQL("cinepedia").query_db(query, data)
        pelicula = cls(result[0])
        return pelicula

    @classmethod
    def read_all(cls):
        query = "SELECT peliculas.*, users.first_name as user_name FROM peliculas JOIN users ON peliculas.user_id = users.id;"
        results = connectToMySQL("cinepedia").query_db(query)
        peliculas = []
        for peli in results:
            peliculas.append(cls(peli))
        return peliculas

    @staticmethod
    def validate_peli(form):
        is_valid = True

        if len(form["nombre"]) < 3:
            flash("El nombre de la pelicula debe tener al menos 3 caracteres","peli")
            is_valid = False

        if len(form["director"]) < 3:
            flash("El director de la pelicula debe tener al menos 3 caracteres", "peli")
            is_valid = False

        if len(form["sinopsis"]) < 3:
            flash("La sinopsis de la pelicula debe tener al menos 3 caracteres","peli")
            is_valid = False

        if form["fecha"] == "":
            flash("Ingresa una fecha de estreno","peli")
            is_valid = False

        return is_valid

    @classmethod
    def delete(cls,data):
        #data = {"id":id}
        query = "DELETE FROM peliculas WHERE id = %(id)s"
        return connectToMySQL("cinepedia").query_db(query,data)

    @classmethod
    def update(cls,form):
        query = "UPDATE peliculas SET nombre = %(nombre)s, director = %(director)s, fecha = %(fecha)s, sinopsis = %(sinopsis)s, user_id = %(user_id)s WHERE id = %(id)s"
        return connectToMySQL("cinepedia").query_db(query, form)