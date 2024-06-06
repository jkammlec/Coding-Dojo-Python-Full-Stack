#from Archivo import Clase
from Animal import Animal

#clase hija(madre)
class Gato(Animal):
    def __init__(self,nombre,sonido,tipo_pelaje):
        super().__init__(nombre,sonido)
        self.tipo_pelaje = tipo_pelaje

    def rascar_sofa(self):
        print(f"{self.nombre} está rascando el sofá de su casa")

    #sobreescritura/anulación
    def hacer_sonido(self):
        print(f"El gato te ve un momento, dice: {self.sonido} y sale corriendo")

    def ir_al_bano(self):
        print(f"{self.nombre} va a su caja, rasca la arena y hace del 1 o el 2")