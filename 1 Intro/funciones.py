#Función: un bloque de código dedicado a una tarea específica que puede invocarse/llamarse las veces que se necesite.

def saludo(): #def: define -> Definiendo una función
    print("Hola mundo!!")

def saludoNombre(nombre):
    print(f"¡Hola {nombre}!")

def saludoLista(lista):
    for nombre in lista:
        print(f"¡Hola {nombre}!")

saludo()
saludo()
saludoNombre("Elena")
saludoNombre("Juana")
saludoLista(["Elena","Juana","Pedro"])

def sumatoria(num1, num2):
    print(num1+num2)

sumatoria(5,6)

def sumatoriaReturn(num1,num2):
    return num1+num2

resultado = sumatoriaReturn(5,6)+sumatoriaReturn(7,7)
print(resultado)

#Ejemplo de función dentro de una función
def funcion():
    print("Hola")
    def funcionDentro():
        print("Dentro de la funcion")
    funcionDentro()

funcion()

def hello(nombre="Elena",apellido="De Troya"):
    print(f"¡Hola {nombre} {apellido}!")

hello()
hello("Juana") #Si no especifico que parámetro es, lo relevante es el orden
hello(apellido="De Arco") #Al especificar el parámetro, ese sería el valor de la variable
hello(apellido="De Arco",nombre="Juana")
hello("Juana","De Arco")

def multiplicacion(num1=1, num2=1):
    return num1*num2

print(multiplicacion())
print(multiplicacion(4))
print(multiplicacion(4,5))

#Función que reciba un arreglo y que regrese la suma de los valores del arreglo
#Ej: [1, 2, 3, 4] return 10

def sum(arr):
    suma = 0
    for num in arr:
        suma += num
    return suma
lista = [1,2,3,4]
print(sum(lista))

#Función que reciba un arreglo y que regrese el número mayor del arreglo
#Ej: [2, 4, 10] return 10
def mayor(arr):
    max = arr[0]
    for num in arr:
        if max < num:
            max = num
    return max
lista2 = [3,4,2,6,1]
print(mayor(lista2))

def numMayor(arreglo):
    return max(arreglo)
arreglo = [2, 4, 10]
print(numMayor(arreglo))

#Función que reciba un arreglo y reciba un número y regrese True si el número se encuentra dentro del arreglo o False si NO se encuentra en el arreglo
#Ej: [2, 4, 6], 1 return False
#Ej: [2, 4, 6], 2 return True

def existe(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
    return False


lista3 = [5, 3, 2, 1, 6]
print(existe(lista3, 8))

arreglo2 = [2, 4, 6]
def findNumber(arreglo, num):  # Agregamos num como parámetro
    if num in arreglo: #in es función integrada de Python
        return True
    else:
        return False
num = int(input("Ingrese un número entero de 1 a 10: "))
resultado = findNumber(arreglo2, num)  # Pasamos num a la función
print(resultado)

#Función que reciba un arreglo y reemplace cualquier número negativo por 0. Regresa el arreglo SIN números negativos. Ej. Recibes: [1,5,10,-2], Regresas [1,5,10,0]

def positivo(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            print(arr[i])
            arr[i] = 0
            print(arr[i])
    return arr
lista4=[1,5,10,-2]
print(positivo(lista4))