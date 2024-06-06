from Animal import Animal
class Persona:
    #Atributo de clase: es un atributo que pertenece a la clase completa
    #y que el valor es compartido por todas las instancias
    escuela = "Coding Dojo LATAM"
    lista_personas = []

    #Método constructor: se encarga de inicializar el objeto
    def __init__(self,nombre,apellido,email,edad,nombre_mascota,sonido_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.lineas_codigo = 0
        self.edad = edad
        self.mascota = Animal(nombre_mascota,sonido_mascota)

        #Cada nueva instancia se agrega a la lista de personas
        Persona.lista_personas.append(self)
    #self = elena
    def imprimir(self):
        print(self.nombre,self.apellido,self.email)
    #self es el objeto que invoca la función
    #self = elena o juana
    def saludar(self):
        print(f"Te saluda {self.nombre}. ¡Holiiii!")

    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas

    @classmethod
    def imprimir_todos(cls): #cls se refiere a la clase que invoca el método
        for p in cls.lista_personas:
            p.imprimir()

    @staticmethod
    def mayor_edad(edad):
        if edad < 18:
            return False
        else:
            return True

    def licencia_conducir(self):
        if(Persona.mayor_edad(self.edad)):
            print("Puedes obtener tu licencia")
        else:
            print("No tienes la mayoría de edad")

    def pasear_mascota(self):
        print("Estas paseando a tu mascota, y como se puso feliz hizo un sonido")
        self.mascota.hacer_sonido()