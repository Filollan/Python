class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        
def posorden(raiz):
     if raiz:
        posorden(raiz.izquierdo)
        posorden(raiz.derecho)
        print(raiz.valor)
            
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

print("Recorrido en preorden del arbol: ")
posorden(raiz)
    