"""Importamos el módulo timeit para medir el tiempo de ejecución, 
   este modulo lo usamos porque el codigo se ejecuta demasiado rapido 
   y no se podia medir con presicion con el modulo time"""
import timeit
#Recursividad

"""Defimos la función potencia_recursiva(), que calcula la potencia de un número utilizando la recursividad"""
def potencia_recursiva(base, exp):
    
    """ Si el exponente es 0, la potencia es 1, de lo contrario,
    la potencia es la base multiplicada por sí misma, el exponente veces"""
    
    if exp == 0:
        return 1
    return base ** exp


#Tiempo con recursividad
"""Imprimimos el tiempo de ejecución de la función potencia_recursiva() 10000 veces.
   Ademas usamos lambda porque se utiliza como un argumento para timeit.timeit(), 
   esta funcion no tiene nombre pero tomas los argumentos de (2, 5) y llama a la funcion potencia_recursiva dentro de ella"""
   
   
tiempo_recursiva = timeit.timeit(lambda: potencia_recursiva(2, 2), number=10000)
print(f"La potencia es {potencia_recursiva(2, 2)}")
print(f"Tiempo de ejecución (Recursiva): {tiempo_recursiva} segundos")

#For

"""Definimos la función potencia_for(), que calcula la potencia de un número utilizando un bucle for"""
def potencia_for(base, exponente):
    """La variable resultado se inicializa a 1, en cada iteración, el valor de resultado 
       se multiplica por base y al final la función devuelve resultado"""
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

#Tiempo con For

"""Imprimimos el tiempo de ejecución de la función potencia_for() 10000 veces"""
tiempo_for = timeit.timeit(lambda: potencia_for(2, 2), number=10000)
print(f"La potencia es {potencia_for(2, 2)}")
print(f"Tiempo de ejecución (For): {tiempo_for} segundos")


