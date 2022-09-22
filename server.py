import socket
from datetime import datetime
from tempfile import tempdir
import json as jn

#recevePackage(tcp)

HOST = '127.0.0.1'  #server IP
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Colocando um endereço IP e uma porta no Socket
host_port = (HOST, PORT)
tcp.bind(host_port)
 
# waiting for the client
tcp.listen(1)

print('\nServidor iniciado no IP número', HOST, 'e na porta', PORT)

conn, client = tcp.accept()
print('\nConexão realizada com ', client)

f1 = 0
while True:
  text = conn.recv(4)
  fin = conn.recv(1)

  if fin.decode() == '1':
    print('Sem mais dados do cliente ' + str(client))
    conn.close()
    break
  
  ack = conn.recv(1)
  pkgN = conn.recv(2)
  
  tempoAtual = datetime.now().strftime('%H:%M:%S')
  print(f'{pkgN.decode()} - recebido: {text.decode()} Flags: {fin.decode()}, {ack.decode()}')

  # check for errors in flag
  ack = ack.decode()
  if ack != 0:
    print("Erro!")
    error_flag = 'A mensagem foi recebida com erro, reenvie'
    conn.sendall(error_flag)
  
  print('Enviando o dado para o cliente.')
  conn.sendall(text)
  