class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        
def inorden(raiz):
     if raiz:
        inorden(raiz.izquierdo)
        print(raiz.valor)
        inorden(raiz.derecho)
            
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

print("Recorrido en preorden del arbol: ")
inorden(raiz)
    