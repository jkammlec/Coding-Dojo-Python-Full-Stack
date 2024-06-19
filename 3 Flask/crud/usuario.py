from mysqlconnection import connectToMySQL
class Usuario:
    def __init__(self, data):
        '''
        data = {
            "id"=1,
            "nombre"="Elena"
            "apellido"="De Troya"
            "email"="elena@email.com"
        }
        '''
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["nombre"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    #Método que realice las consultas
    # formulario = {"nombre":"ELena",
    # "apellido:"De Troya".....}
    @classmethod
    def guardar(cls, formulario):
        # formulario = {"nombre": "Juana", "apellido": "De Arco"....}
        consulta = "INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s);"
        resultado = connectToMySQL("crud_bc").query_db(consulta, formulario)
        return resultado  # el id del nuevo registro

    #Método que regrese todos los usuarios
    @classmethod
    def mostrar_usuarios(cls):
        query = "SELECT * FROM usuarios;"
        resultado = connectToMySQL("crud_bc").query_db(query)
        #resultado = [{lista de diccionarios}]
        usuarios = []
        for u in resultado:
            usuarios.append(cls(u)) #1- cls(u) me genera la instancia de usuario 2- la instancia se agrega a la lista
        return usuarios

    @classmethod
    def borrar(cls,data):
        query = "DELETE FROM usuarios WHERE id = %(id)s"
        return connectToMySQL('crud_bc').query_db(query,data)

    @classmethod
    def mostrar_un_usuario(cls,data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        resultado = connectToMySQL('crud_bc').query_db(query,data)
        #resultado = [{"id":1,"nombre":"Elena","apellido":"De Troya"}]
        usuario = cls(resultado[0]) #creo el objeto/instancia con la info de la bd
        return usuario #instancia de usuario

    @classmethod
    def actualizar_usuario(cls,formulario):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s WHERE id=%(id)s"
        return connectToMySQL('crud_bc').query_db(query, formulario)