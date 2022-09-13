import socket

HOST = '127.0.0.1'  #server IP
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Colocando um endereço IP e uma porta no Socket
host_port = (HOST, PORT)
tcp.bind(host_port)
 
# Esperando o cliente falar algo
tcp.listen(1)

print('\nServidor iniciado no IP número', HOST, 'e na porta', PORT)
print('Servidor ligado, ok\n')

while True:
  conexao, cliente = tcp.accept()
  print('\nConexão realizada por:', cliente)

  texto = conexao.recv(1024)
  print("Mensagem: ", texto.decode())
