import socket
import sys
import time

#res = ''.join(format(ord(i), '08b') for i in test_str)

def sendPackage(mens, server):
    mens = ''.join(format(ord(i), '08b') for i in mens)
    k = int(len(mens)/8)
    m = mens[0:k]
    print('- ' + m) 
    server.sendall(m.encode())
    for c in range(2,9):
        m = mens[(c-1)*k:c*k]
        print('- ' + m)
        server.sendall(m.encode())

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
print("Digite seu nome:")
name = input(": ")

sendPackage(name, conn)

#conn.sendall(name.encode())

print("Digite algo!")
while True:
    message_client = input("- ")
    size_message = str(len(message_client))
    if size_message == "0":
        print("Mensagem vazia!, nao enviada!")
    else:
        conn.sendall(size_message.encode())
        conn.sendall(message_client.encode())

