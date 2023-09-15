import time 
inicio=time.time()


def contador(num):
     print(num, end=" -> ")
     if num == 1:
        return
     else:
        return contador(num-1)

num=int(input("Digita el numero: "))    
contador(num)

fin =time.time()
tiempo_ejecucion=fin -inicio
print(f"el tiempo de ejecucion es: {tiempo_ejecucion}")