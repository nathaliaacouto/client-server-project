import socket
import sys

host = str(input(": "))
port = int(input(": "))
h_p = (host, port)

try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(h_p)

<<<<<<< HEAD
except:
    print("Não foi possivel conectar no servidor!")
=======
except TimeoutError:
    print("Não foi possivel conectar no servidor!")
    sys.exit(0)

except ConnectionRefusedError:
    print("Porta incorreta!")
    sys.exit(0)

except:
    print("Incapaz de conectar no servidor!")
    sys.exit(0)

print("Conectado ao servidor!")



>>>>>>> edc73e5ba7d2a1e3466343660c7b846910270d87
