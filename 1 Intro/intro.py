print("Hola mundo!")
#booleans
booleano = True #True or False
#numeros
num = 10 #numero entero
fl = 10.99 #float / con punto decimal
nuevo_float = float(num) #forzar numero entero a ser flotante
print(nuevo_float)
nuevo_entero = int(fl)
print(nuevo_entero)
print(round(fl))

import random #importando librería random

num_aleatorio = random.randint(1, 5)
print(num_aleatorio)

#cadenas/textos/strings

abc = "ABCDEFG"
otro_texto = "Otro texto."
print("Este es el abecedario:", abc) #la coma agrega un espacio entre los textos
print("Este es el abecedario: "+ abc) #el + concatena las cadenas tal cual
print(otro_texto+" "+abc)
print(otro_texto,abc)
print("Este es un número:",num)
print("Este es un numero: "+str(num))
nombre = "Juana"
apodo = "Juanita"
print(f"Hola, te presento a {nombre}, le puedes llamar '{apodo}'.") #Interpolación
print("Hola, te presento a "+nombre+", le puedes llamar '"+apodo+"'.")

#métodos de manipulación de cadena
frase = "hola mundo! soy Juana de Arco y hoy es 27 de Mayo"
print(frase.title()) #Primera letra de cada palabra en mayúscula (capitalizar)
print(frase.upper()) #Todo en mayúsculas
print(frase.lower()) #Todo en minúsculas
print(frase.count('oy')) #Devuelve cuántos 'oy' hay en la cadena
print(frase.find('Juana')) #Devuelve el índice en el que está la palabra (case sensitive)
print(frase[-1]) #Devuelve la última letra de la frase

#Estructuras de datos
#Tuplas: es parecido a un arreglo, pero sus valores no se pueden cambiar
tupla = ("Elena", "Juana", "Pedro", "Pablo")
print(tupla[0]) #tupla[indice]
#tupla[1] = "Juanita" TypeError: 'tuple' object does not support item assignment
tupla2 = ("texto",7,False,6.6) #Pueden tener distintos tipos de datos

#LISTAS / ARRAY / ARREGLO
lista_nombres = ["Hugo","Paco","Luis"]
print(lista_nombres[2])
lista_nombres[2] = "Donald"
print(lista_nombres)
lista_nombres.pop() #Elimina la última posición de la lista
print(lista_nombres)
lista_nombres.pop(0)
print(lista_nombres)
lista_nombres.append("Mickey") #Agrega un elemento al final de la lista
print(lista_nombres)
lista_nombres.insert(1,"Goofy")
print(lista_nombres)
lista_mix = ["texto",11,True,1.1,["elemento1","elemento2"]]
matriz = [
    [0,1,2,3,4],
    [5,6,7,8,9]
]
print(matriz[1][2])
#Diccionarios

estudiante = {
    "nombre":"Juana",
    "apellido":"De Arco",
    "edad":18,
    "soltera":True,
    "hobbies":["leer","comer","salir al parque"]
}

print(estudiante["nombre"])
estudiante["edad"]= 19
print(estudiante)
estudiante["estatura"]=1.67
print(estudiante)
estudiante.pop("soltera") #Elimina el par de clave-valor
print(estudiante)

lista_alumnos = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]

#¿Cómo eliminamos de la lista de cursos MERN para Pedro?
#lista_alumnos[2]["cursos"].pop(2) #elimina el indice
lista_alumnos[2]["cursos"].remove("MERN") #elimina el valor
print(lista_alumnos)
'''
Comentarios
mas extensos
'''
from pprint import pprint #Importando la función pprint de la librería pprint
pprint(lista_alumnos)

