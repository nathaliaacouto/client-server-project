import socket
import sys

host = str(input(": "))
port = int(input(": "))
h_p = (host, port)

try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(h_p)

except TimeoutError:
    print("Não foi possivel conectar no servidor!")

except ConnectionRefusedError:
    print("Porta incorreta!")

finally:
    print("Incapaz de conectar no servidor!")
    sys.exit(0)

print("Conectado ao servidor!")



