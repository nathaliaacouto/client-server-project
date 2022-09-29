import socket
from datetime import datetime
from tempfile import tempdir
import json as jn

#recevePackage(tcp)

HOST = '127.0.0.1'  #server IP
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_port = (HOST, PORT)
tcp.bind(host_port)
 
# waiting for the client
tcp.listen(1)

print('\nServidor iniciado no IP número', HOST, 'e na porta', PORT)

conn, client = tcp.accept()
print('\nConexão realizada com ', client)

string = ''
while True:

  # Timeout
  conn.settimeout(10)
  text = conn.recv(4)
  fin = conn.recv(1)

  if fin.decode() == '1':
    print('Sem mais dados do cliente ' + str(client))
    conn.close()
    break
  
  ack = conn.recv(1)
  ##wdw = conn.recv(1)
  end = conn.recv(1)
  pkgN = conn.recv(1)
  string = string + str(text.decode())

  tempoAtual = datetime.now().strftime('%H:%M:%S')
  print(f'{pkgN.decode()} - recebido: {text.decode()} | Flags: {fin.decode()}, {ack.decode()}')

  # check for errors in the flag
  ack = ack.decode()
  if ack != '0':
    print("Mensagem recebida com erro!")
    error_message = 'O pacote foi recebida com erro, reenvie'
    conn.sendall(error_message.encode())
    conn.send(text)
  else:
    print('Enviando o dado para o cliente.')
    conn.sendall(text)

  end = end.decode()
  if end == '1':
    if conn.recv(2).decode() == str(len(string)):
      print('--- Mensagem ecoada: ' + string + ' ---')
    else:
      print('Erro presente na mensagem!')
    string = ''
