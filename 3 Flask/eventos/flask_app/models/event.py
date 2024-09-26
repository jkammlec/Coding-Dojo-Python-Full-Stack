from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Event:

    def __init__(self,data):
        #data = {diccionario con la info de la bd}
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.date = data["date"]
        self.details = data["details"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.image = data["image"]

        self.user_name = data["user_name"] #columna extra al hacer una consulta join

    @classmethod
    def create(cls,form):
        #form = {"name":"Examen de Python","location":"Casa"...}
        query = "INSERT INTO events (name, location, date, details, user_id) VALUES (%(name)s,%(location)s,%(date)s,%(details)s,%(user_id)s)"
        return connectToMySQL("events_bc").query_db(query, form)

    @classmethod
    def read_one(cls,data):
        #data = {"id":1}
        query = "SELECT events.*, users.first_name as user_name FROM events JOIN users ON events.user_id = users.id WHERE events.id = %(id)s;"
        result = connectToMySQL("events_bc").query_db(query, data)
        event = cls(result[0])
        return event

    @classmethod
    def read_all(cls):
        query = "SELECT events.*, users.first_name as user_name FROM events JOIN users ON events.user_id = users.id;"
        results = connectToMySQL("events_bc").query_db(query)
        events = []
        for ev in results:
            events.append(cls(ev)) #ev = {diccionario con la info de bd}, cls(ev): Crear el objeto Event, events.append(): el objeto Event lo agrego a la lista
        return events

    @staticmethod
    def validate_event(form):
        # form = {"name":"Examen de Python","location":"Casa"...}
        is_valid = True

        if len(form["name"]) < 3:
            flash("El nombre del evento debe tener al menos 3 caracteres","evento")
            is_valid = False

        if len(form["location"]) < 3:
            flash("La ubicación del evento debe tener al menos 3 caracteres", "evento")
            is_valid = False

        if len(form["details"]) < 3:
            flash("Los detalles del evento deben tener al menos 3 caracteres","evento")
            is_valid = False

        if form["date"] == "":
            flash("Ingresa una fecha","evento")
            is_valid = False

        return is_valid

    @classmethod
    def delete(cls,data):
        #data = {"id":id}
        query = "DELETE FROM events WHERE id = %(id)s"
        return connectToMySQL("events_bc").query_db(query,data)

    @classmethod
    def update(cls,form):
        query = "UPDATE events SET name = %(name)s, location = %(location)s, date = %(date)s, details = %(details)s, user_id = %(user_id)s WHERE id = %(id)s"
        return connectToMySQL("events_bc").query_db(query, form)