import time

inicio=time.time()
for _ in range(1000000):
    pass
# Esta función calcula el número de Fibonacci en la posición n.
def fibonacci(n):
     
     
     # Si el número es 0 o 1, entonces el número de Fibonacci es el mismo que el número.
    if n == 0 or n == 1:
        return n
    # De lo contrario, el número de Fibonacci es la suma de los dos números de Fibonacci anteriores.
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

for i in range(11):
    print(f"El numero es {fibonacci(i)}")
    
 
fin =time.time()
tiempo_ejecucion=fin -inicio
print(f"el tiempo de ejecucion es: {tiempo_ejecucion}")


