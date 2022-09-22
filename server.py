import socket
from datetime import datetime
from tempfile import tempdir

#recevePackage(tcp)

HOST = '127.0.0.1'  #server IP
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Colocando um endereço IP e uma porta no Socket
host_port = (HOST, PORT)
tcp.bind(host_port)
 
# Esperando o cliente falar algo
tcp.listen(1)

print('\nServidor iniciado no IP número', HOST, 'e na porta', PORT)

conexao, cliente = tcp.accept()
print('\nConexão realizada com ', cliente)

f1 = 0
while True:

  texto = conexao.recv(4)
  fin = conexao.recv(1)

  if fin.decode() == '1':
    print('Sem mais dados do cliente ' + str(cliente))
    conexao.close()
    break
  
  ack = conexao.recv(1)
  pkgN = conexao.recv(2)
  
  tempoAtual = datetime.now().strftime('%H:%M:%S')
  print(f'{pkgN.decode()} - recebido: {texto.decode()} Flags: {fin.decode()}, {ack.decode()}')
  print('Enviando o dado para o cliente.')
  conexao.sendall(texto)
  