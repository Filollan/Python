import time 
inicio=time.time()
#Recursivamente
def suma(lista):
  if len(lista) == 1:   # Caso base
    return lista[0]
  else:
    return lista[0] + suma(lista[1:]) # La función se llama a si misma (Recursión)
                                          # lista[1:] devuelve la lista sin su primer elemento
print(suma([1,2,3,4,5,6,7]))

fin =time.time()
tiempo_ejecucion=fin -inicio
print(f"el tiempo de ejecucion es: {tiempo_ejecucion}")
 
#For
inicio=time.time()
def suma(lista):
  suma = 0
  # Suma cada numero de la lista.
  for i in range(0,len(lista)):
    suma = suma + lista[i]
  # Devuelve la suma
  return suma
print(suma([1,2,3,4,5,6,7]))
fin =time.time()
tiempo_ejecucion=fin -inicio
print(f"el tiempo de ejecucion es: {tiempo_ejecucion}")
    