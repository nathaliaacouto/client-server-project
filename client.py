import socket

host = str(input(": "))
port = int(input(": "))
h_p = (host, port)

try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(h_p)

except:
    print("Não foi possivel conectar no servidor!")
    

