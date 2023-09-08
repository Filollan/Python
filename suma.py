# Define an array of 10 numbers
numeros = []

# GObtener los 10 numeros
for i in range(10):
    numero = int(input("Ingrese el numero: "))
    numeros.append(numero)

# Suma del array
suma = 0
for numero in numeros:
    suma += numero

# Multiplicacion del array
multiplicacion = 1
for numero in numeros:
    multiplicacion *= numero

# Promedio del array
promedio = suma / len(numeros)

# Resultados
print("La suma del arreglo es: ", suma)
print("La multiplicacion del arreglo es: ", multiplicacion)
print("El promedio del arreglo es: ", promedio)