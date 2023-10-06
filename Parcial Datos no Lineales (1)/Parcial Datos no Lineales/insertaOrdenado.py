class Nodo:
    """Clase que representa un nodo en un árbol binario."""

    def __init__(self, valor):
        """Inicializa un nuevo nodo con el valor dado."""
        self.valor = valor
        self.izquierdo = None
        self.derecha = None



def insertar(raiz, valor):
    """Inserta un nuevo nodo en un árbol binario."""
    # Verifica si el árbol es vacío.
    if raiz is None:
        return Nodo(valor)

    # Verifica si el valor dado es menor que el valor del nodo actual.
    if valor < raiz.valor:
        raiz.izquierdo = insertar(raiz.izquierdo, valor)
    else:
        raiz.derecha = insertar(raiz.derecha, valor)

    return raiz


def recorrer_inorden(raiz):
    """Recorre un árbol binario en orden inorden."""
    # Verifica si el árbol es vacío.
    if raiz is None:
        return

    # Recorre el subárbol izquierdo.
    recorrer_inorden(raiz.izquierdo)

    # Imprime el valor del nodo actual.
    print(raiz.valor)

    # Recorre el subárbol derecho.
    recorrer_inorden(raiz.derecha)


if __name__ == "__main__":
    # Crea un árbol binario con los valores dados.
    raiz = None
    valores = [20, 2, 18, 14, 5]
    for valor in valores:
        raiz = insertar(raiz, valor)

    # Inserta un nuevo nodo con el valor 10.
    raiz = insertar(raiz, 10)

    # Recorre el árbol binario en orden inorden.
    recorrer_inorden(raiz)