import socket
from datetime import datetime
from tempfile import tempdir


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
nome = conexao.recv(1024)
nome = nome.decode()
print('\nConexão realizada por:', nome)

while True:
  tamanho_mensagem = conexao.recv(1024)
  texto = conexao.recv(1024)

  print(len(texto))
  print(tamanho_mensagem.decode())


  if len(texto) != int(tamanho_mensagem.decode()):
    print("[X] - Tamanho da mensagem incompatível!")
  else:
    tempoAtual = datetime.now().strftime('%H:%M:%S')
    print(f'{tempoAtual} - {nome} diz: {texto.decode()}')
