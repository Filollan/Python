import time
import threading

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def calcular_factorial(inicia, termina):
    for numero in range(inicia, termina + 1):
        factorial_resultado = factorial(numero)
        print(f"El factorial de {numero} es {factorial_resultado}")
        
    # Imprimir los elementos de la lista enlazada
    

hilo1 = threading.Thread(target=calcular_factorial, args=(1,10))
hilo2 = threading.Thread(target=calcular_factorial, args=(11,20))

inicio = time.time()
hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Todos los hilos terminaron ")

fin = time.time()

tiempo_ejecucion = fin- inicio
print(f"El tiempo de ejecución fue de: {tiempo_ejecucion}")