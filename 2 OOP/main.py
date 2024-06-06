#importar la clase
from Persona import Persona
from Animal import Animal
from Gato  import Gato
from Perro import Perro

ragnar = Animal("Ragnar","miau")
firulais = Animal("Firulais","guau")

elena = Persona("Elena","De Troya","elena@email.com",18,"ragnar","miau") #creando la instancia de Persona
juana = Persona("Juana","De Arco","juana@email.com",22,"firulais","woof")
print(elena.nombre)
print(juana.nombre)
elena.imprimir()

juana.saludar()
elena.saludar()

juana.codificar(15)
juana.codificar(100)
print(juana.lineas_codigo)

print(juana.escuela)
print(elena.escuela)

#Cambiando para toda la clase la escuela
Persona.escuela = "Escuela de programación"
print(juana.escuela)
print(elena.escuela)

pedro = Persona("Pedro","Paramo","pedro@email.com",32,"Snoopy","woof")

print(len(Persona.lista_personas))
Persona.imprimir_todos()
pedro.licencia_conducir()
pedro.mascota.hacer_sonido()

michi = Gato("Penchan","miau","largo")
cholo = Perro("Cholito","guau","quiltro")

michi.rascar_sofa()
michi.hacer_sonido()
cholo.hacer_sonido()
cholo.perseguir_autos()
michi.ir_al_bano()
cholo.ir_al_bano()