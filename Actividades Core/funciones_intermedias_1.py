#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz = [ [10, 15, 20], [3, 7, 14] ]

matriz[1][0] = 6
print(matriz)

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

#En ciudades, cambia “Cancún” por “Monterrey”
cantantes[0]["nombre"]="Enrique Martin Morales"
print(cantantes[0])

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

ciudades["México"][2]="Monterrey"
print(ciudades["México"])

#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]
coordenadas[0]["latitud"]=9.9355431
print(coordenadas)

#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios
#y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.
cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario2(llave,lista):
    for dicc in lista:
        print(dicc[llave])

iterarDiccionario2("nombre",cantantes)

#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función
# debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def imprimirInformacion(diccionario):
    for clave in diccionario:
        lista = diccionario[clave]
        print(len(lista), clave.upper())
        for elemento in lista:
            print(elemento)

imprimirInformacion(costa_rica)