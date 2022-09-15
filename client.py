import socket
import sys

# host = str(input(": "))
# port = int(input(": "))

host = str("127.0.0.1") # DEBUG
port = int(5000) # DEBUG

h_p = (host, port)

try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(h_p)

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
print("Digite seu nome:")
name = input(": ")
conn.sendall(name.encode())

print("Digite algo!")
while True:
    message_client = input("- ")
    size_message = str(len(message_client))
    if size_message == "0":
        print("Mensagem vazia!, nao enviada!")
    else:
        conn.sendall(size_message.encode())
        conn.sendall(message_client.encode())
