import time
inicio=time.time()
def es_primo(numero):#la definicion de una funcion def
    
    for i in range(2, numero//2+1):
        if numero %i ==0:
            return False
    return True

contador=0
numero=2
while (contador<1000):
    if es_primo(numero):
        print(numero, end=" => ") 
      
        contador+=1
    numero+=1
for _ in range(1000):
    pass    
    fin =time.time()
tiempo_ejecucion=fin -inicio
print()
print(f"El tiempo de ejecucion es: {tiempo_ejecucion}")
            