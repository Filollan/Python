import socket

def scanear_puerto(ip, puertos):
    for puerto in puertos:
        sock = socket .socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.1)
        result = sock.connect_ex((ip, puerto))
        if result == 0:
            print(f"puerto {puerto} abierto")
        else:
            sock.close()

if __name__  == "__main__":
    ip = '172.67.163.111'
    puertosA = range(1, 1025)

scanear_puerto(ip, puertosA)