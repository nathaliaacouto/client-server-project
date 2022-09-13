import socket

host = str(input(": "))
port = int(input(": "))

h_p = (host, port)
socket.connect(h_p)