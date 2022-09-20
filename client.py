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

print("Conectado ao servidor!")
print('Digite "-1" para finalizar a conexão')
while True:
    message_client = input(": ")
    sm = len(message_client)
    conn.sendall(message_client.encode())
    if message_client == '-1':
        conn.close()
        break
    c = 0
    while True:
        massage_server = conn.recv(4)
        # m = message_client[c:c+4] mensagem que foi enviada/recebida
        c = c + 4
        print('Recebido: ' + str(massage_server.decode()))
        if c >= sm:
            break
