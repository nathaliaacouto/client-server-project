import socket
import sys
import time

# host = str(input(": "))
# port = int(input(": "))

host = str("127.0.0.1") # DEBUG
port = int(5000) # DEBUG

hostPort = (host, port)

while True:    
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        start = time.perf_counter()
        conn.connect(hostPort)
        print("Time to connect: " + str((time.perf_counter() - start) * 1000) + "ms")
        break

    except TimeoutError:
        print("Não foi possivel conectar no servidor!")
        # sys.exit(0)

    except ConnectionRefusedError:
        print("Porta incorreta!")
        # sys.exit(0)

    except:
        print("Incapaz de conectar no servidor!")
        # sys.exit(0)

print("Conectado ao servidor!", end="\n")
while True:
    message_client = input("- ")
    sm = len(message_client)/8
    print(round(sm))

    for c in range(7):
        m = message_client[c*sm:(c+1)*sm]
        conn.sendall(message_client.encode())
        massage_server = conn.recv(1024)
        print('Dados recebidos: ' + str(massage_server.decode()))
