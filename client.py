import socket
import sys
import time
import json as jn

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
    FIN = 0
    ACK = 0

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
        #Send
        mens = message_client[4*Npckg:4*(Npckg+1)]
        conn.send(mens.encode())  
        conn.send(str(FIN).encode()) 
        conn.send(str(ACK).encode())  #error flag 
        conn.send(str(Npckg).encode())  
        
        message_server = conn.recv(4)
        print('Recebido: ' + str(message_server.decode()) + ' Número = ', Npckg)
        Npckg += 1
        i += 4
        if i >= mSize:
            break
    
    client_choose = input("você quer simular um erro na mensagem passada?\n1 - sim \n2 - não\nescolha- ")
    if client_choose == '1':
        pckgNum = input('Qual o pacote que deve conter o erro? ')

        Npckg = 0
        i = 0
        while True:

            if Npckg == int(pckgNum):
                # Simulation of a currupt/lost package
                mens = 'e404'
                conn.send(mens.encode())  
                conn.send(str(FIN).encode()) 
                conn.send(str(1).encode())  #error flag 
                conn.send(str(Npckg).encode())  
                message_server = conn.recv(41)
                text_server = conn.recv(4)
                print('Recebido: ' + str(message_server.decode()) + ' Número = ', Npckg)
                
                # Validate if the server message is different from the original
                if (message_client[4*Npckg:4*(Npckg+1)]) != (text_server.decode()):
                    print('Mensagem recebida pelo servidor é diferente da enviada pelo cliente')
                    print('Reenviando pacote')

             
            mens = message_client[4*Npckg:4*(Npckg+1)]
            conn.send(mens.encode())  
            conn.send(str(FIN).encode()) 
            conn.send(str(ACK).encode())  #error flag 
            conn.send(str(Npckg).encode())  
                
            message_server = conn.recv(4)
            print('Recebido: ' + str(message_server.decode()) + ' Número = ', Npckg)
            Npckg += 1
            i += 4
            if i >= mSize:
                break
