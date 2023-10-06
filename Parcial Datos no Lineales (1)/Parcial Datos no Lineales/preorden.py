class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        
def preorden(raiz):
     if raiz:
        print(raiz.valor)
        preorden(raiz.izquierdo)
        preorden(raiz.derecho)
            
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

print("Recorrido en preorden del arbol: ")
preorden(raiz)
    