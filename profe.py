n = int(input("Ingrese la cantidad de numeros: "))

numeros = []
pares = []
impares = []

for i in range(n):
    numero = float(input(f"Ingrese el numero {i+1}: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

multiplicacion = 1.0
for num in numeros:
    multiplicacion *= num

if n % 2 == 0:
    print(n, "es par.")
else:
    print(n, "es impar.")

suma_pares = sum(pares)
suma_impares = sum(impares)


print(f"La suma de los pares es: {suma_pares}")
print(f"La suma de los impares es: {suma_impares}")
print(f"La suma de los numeros es: {sum(numeros)}")
print(f"La multiplicacion es: {multiplicacion}")
