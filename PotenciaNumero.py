import time

inicio=time.time()
for _ in range(1000000):
    pass
def potencia(base, exponente):
  

   
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)




print(f"La potencia es {potencia(2, 5)}")
fin =time.time()
tiempo_ejecucion=fin -inicio
print(f"el tiempo de ejecucion es: {tiempo_ejecucion}")
