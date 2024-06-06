#Básico: imprime todos los números enteros del 0 al 100.
for x in range(101):
    print(x)

#Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for y in range(501):
    if y%2==0:
        print(y)

#Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número.
# Si es divisible por 10, imprime “baby”
for z in range(101):
    if z%10==0:
        print("baby")
    elif z%5==0:
        print("ice ice")
    else:
        print(z)

#Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
suma = 0
for n in range(0,500001):
    if n%2==0:
        suma += n
    print(suma)

#Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

for x in range(2025,0,-3):
    print(x)

#Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal,
#imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2,
# el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

num_inicial = 3
num_final = 10
multiplo = 2

for num in range(num_inicial,num_final+1):
    if num%multiplo==0:
        print(num)