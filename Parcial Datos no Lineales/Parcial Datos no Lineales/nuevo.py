""" 1.  Que características se pueden mejorar y en que consiste
    2. Que alternativas existen para realizar la misma tarea
    3. Codificar la mejorar
    4. Demostrar que funciona la optimización 
    
     def p(base, exp):

    if exponente == 0:

        return 1

    resultado = -1

    for _ in range(exponente):

        resultado *= base

    return resultado
    """
import time
#codigo profesor
inicio=time.time()
def p(base, exponente):

    if exponente == 0:

        return 1

    resultado = 1

    for _ in range(exponente):

        resultado *= base

    return resultado
print(f"La potencia es {p(4,2)}")
fin =time.time()
tiempo_ejecucion=fin -inicio
print(f"el tiempo de ejecucion del codigo del profesor es: {tiempo_ejecucion}")


