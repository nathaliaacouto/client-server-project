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
    package_num_error = -1

    client_choose = input("\nVocê quer simular um erro?\n1 - sim \n2 - não\nescolha: ")
    if client_choose == '1':
        package_num_error = int(input("Qual o número do pacote em que você quer simular o erro? "))

    ACK = 0
    FIN = 0
    
    message_client = input(": ")

    mSize = len(message_client)
    if message_client == '-1':
        FIN = 1
        conn.send(message_client.encode())
        conn.send(str(FIN).encode())
        conn.close()
        break
    Npckg = 0
    i = 0

    while True:
        mens = message_client[4*Npckg:4*(Npckg+1)]
        conn.send(mens.encode())  
        conn.send(str(FIN).encode()) 
        conn.send(str(ACK).encode())  #flag de erro
        conn.send(str(Npckg).encode())  
        if ACK == 1:
            message_server = conn.recv(200)
            print('Recebido: ' + str(message_server.decode()) + '\nNúmero de sequência = ', Npckg)
        else: 
            message_server = conn.recv(4)
            print('Recebido: ' + str(message_server.decode()) + '\nNúmero de sequência = ', Npckg)
        Npckg += 1
        i += 4
        if i >= mSize:
            break