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

def es_primo(numero):
    for i in range (2, numero//2+1):
        if numero % i == 0:
            return False
    return True

def generar_lista_primos(inicia,termina):

    # Crear una instancia de la lista enlazada y agregar elementos
    mi_lista = ListaEnlazada()
    numero = inicia
    contador = 0
    while(contador<termina):
        if es_primo(numero):
            mi_lista.agregar(numero)
            contador+=1   
        numero+=1
        
    # Imprimir los elementos de la lista enlazada
    mi_lista.imprimir()  

hilo1 = threading.Thread(target=generar_lista_primos, args=(2,2000))
hilo2 = threading.Thread(target=generar_lista_primos, args=(2001,4000))

inicio = time.time()
hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Todos los hilos terminaron ")

fin = time.time()

tiempo_ejecucion = fin- inicio
print(f"El tiempo de ejecución fue de: {tiempo_ejecucion}")