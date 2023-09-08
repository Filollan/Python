import threading

def mi_funcion():
    for _ in range(5):
        print("hola desde el hilo")
mi_hilo= threading.Thread(target=mi_funcion)

mi_hilo.start()

mi_hilo.join()