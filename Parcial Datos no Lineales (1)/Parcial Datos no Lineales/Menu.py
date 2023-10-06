class Nodo:
    def __init__(self, nombre, hijos):
        self.nombre = nombre
        self.hijos = hijos


def crear_arbol_menu():
    raiz = Nodo("menú", [])
    comida_rapida = Nodo("comida rápida", [])
    hamburguesa = Nodo("hamburguesa", [])
    comida_rapida.hijos.append(hamburguesa)
    raiz.hijos.append(comida_rapida)

    perros_calientes = Nodo("perros calientes", [])
    hot_dog = Nodo("hot dog", [])
    perros_calientes.hijos.append(hot_dog)
    comida_rapida.hijos.append(perros_calientes)

    sanwiches = Nodo("sándwiches", [])
    club = Nodo("club", [])
    sanwiches.hijos.append(club)
    comida_rapida.hijos.append(sanwiches)

    return raiz


def buscar_elemento_menu(arbol, nombre, tipo):
    if arbol is None:
        return None

    if arbol.nombre == nombre and arbol.tipo == tipo:
        return arbol

    for hijo in arbol.hijos:
        resultado = buscar_elemento_menu(hijo, nombre, tipo)
        if resultado is not None:
            return resultado

    return None


if __name__ == "__main__":
    arbol = crear_arbol_menu()

    hamburguesa = buscar_elemento_menu(arbol, "hamburguesa", "comida rápida")
    print(hamburguesa.nombre)

    perro_caliente = buscar_elemento_menu(arbol, "perro caliente", "comida rápida")
    print(perro_caliente.nombre)

    sanwich = buscar_elemento_menu(arbol, "sándwich", "comida rápida")
    print(sanwich.nombre)