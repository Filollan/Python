def factorial(n):
    if n == 0:
      return 1 # Caso base
    else:
     return n * factorial(n-1) #caso recursivo
print(f"El fatorial es: {factorial}")