import time


def es_primo(numero):
   for i in range (2,numero//2+1):
      if numero % i == 0:
        return False
   return True


numero = int(input("Ingrese el numero: "))
inicio=time.time()
for _ in range(1000000):
    pass
if es_primo(numero):
    print("EL numero es verdadero")
else:
    print("No es primo")
    
    fin =time.time()
tiempo_ejecucion=fin -inicio
print(f"el tiempo de ejecucion es: {tiempo_ejecucion}")