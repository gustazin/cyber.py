from socket import *

            #loopback
endereco = "127.0.0.1"
porta = 43210 

while True : 
    obj_socket = socket(AF_INET, SOCK_STREAM)

    obj_socket.connect((endereco , porta))
    msg = bytes(input("mensagem : "), 'utf-8')
    obj_socket.send(msg)

resposta = obj_socket.recv(1014)
print("resposta : ", str(resposta)[2:-1])
if str(msg)[2:-1] == "fim":
    break

