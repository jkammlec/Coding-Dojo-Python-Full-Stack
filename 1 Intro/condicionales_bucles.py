#CONDICIONALES

x = 20

if x > 10:
    print("El número ingresado es mayor a 10")
    print(f"El número es: {x}") #Format interpolar variables
    #Otra
    #Otra
else:
    print("El número es menor o igual a 10")

edad_infante = 4
if edad_infante < 2:
    print("Es un bebé")
elif edad_infante < 5:
    print("Es un toddler")
else:
    print("Es un niño")

y = 5
if y > 3:
    print("Numero mayor a 3")
else:
    print("Numero menor o igual a 3")
    print("Tu número es menor a 3")

temperatura = 20
estaLLoviendo = False
if temperatura > 18 and not estaLLoviendo:
    print("Salgamos a pasear al parque")

edad = 17
#print("Ingresa tu edad")
#edad = int(input("Ingresa tu edad: "))
#edad = int(edad)
permisoPadres = True
if edad >= 18 or permisoPadres:
    print("Puedes obtener tu licencia de manejo")
    #otra linea
    #otra linea

#Bucles/Ciclos

for x in range(5): #Rango 0-4. 5 ya no entra. x < 5
    print(x)

print("-----------")

for y in range(5, 12): #(Comienzo, Fin) -> y=5; y<12
    print(y)

print("---------")

for z in range(2,12,2): #(Comienzo,Fin,Pasos) -> z=2; z <12; z+=2
    print(z)

print("---------")

for m in range(30,15,-2):
    print(m)

#Recorrer un arreglo
lista_nombres = ["Elena","Juana","Pablo","Pedro"]
for nombre in lista_nombres:
    print(nombre)
for indice in range(len(lista_nombres)): #i=0; i<4; i=indice
    print(f"Indice: {indice}; Valor: {lista_nombres[indice]}")

estudiante = { #equivalente a objeto en js
    "nombre:":"Elena", #clave: valor
    "apellido:":"De Troya",
    "edad:":19
}

print("-------------")
#clave = "nombre"
#print nombre: Elena
#clave = "apellido"
#print apellido: De Troya
#clave = "edad"
#print edad: 19
for clave in estudiante:
    print(clave, estudiante[clave])

print("---------------")

'''
dato = "nombre"
print Clave:nombre. Valor: Elena
---
dato = "apellido"
print Clave: apellido. Valor: De Troya
---
dato = "edad"
print Clave: edad. Valor: 19
'''

lista_estudiantes = [
    {"Nombre":"Elena","Apellido":"De Troya","id":123},
    {"Nombre": "Juan", "Apellido": "De Arco", "id": 234},
    {"Nombre": "Pedro", "Apellido": "Páramo", "id": 345},
]

for estudiante in lista_estudiantes:
    print(estudiante)
    for dato in estudiante:
        print(f"Clave: {dato}. Valor: {estudiante[dato]}")

print("---------------")

texto = "Buen día"
for letra in texto:
    print(letra)

print("---------------")

inicio = 0
final = 5
'''
inicio = 0
final = 5
imprime: inicio: 0. final: 5
inicio = 1
final = 3
---
imprime: inicio: 1. final: 3
inicio = 2
final = 1
---
'''

while inicio < final:
    print(f"inicio: {inicio}. final: {final}.")
    inicio += 1
    final -= 2

print("---------------")

i = 4
'''
i=4
imprime: Entra a while 4
i=5
---
imprime: Entra a while 5
i=6
---
imprime: Entra a while 6
i=7
---
imprime: Dejo de cumplirse la condicional 7
'''
while i < 7:
    print("Entra a while.",i)
    i += 1
else: #va a entrar después de que deje de cumplirse la condición
    print("Dejó de cumplirse condicional:",i)

print("---------------")

#Break -> interrumpir por completo mi bucle

for x in range(16):
    if x == 13:
        continue #interrupción temporal, el 13 se salta
        #break
    print(x)

#RETO INDIVIDUAL
#Dado el for 1 al 15, imprime todos los numeros EXCEPTO aquellos múltiples de 5. break/continue

for x in range(16):
    if x%5==0:
        continue
    print(x)

#Dada una cadena, imprima cada uno de los caracteres y que se detenga POR COMPLETO si encuentra un . (PUNTO)
cadena1 = "Hola, buenos dias. Como estas"

for letra in cadena1:
    print(letra)
    if letra == ".":
        break