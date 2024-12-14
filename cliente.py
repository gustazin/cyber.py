from socket import * 

endereco = "127.0.0.1"
porta = 43210

obj_socket = socket ( AF_INET, SOCK_STREAM)
obj_socket.bind((endereco , porta))
obj_socket.listen (2)

print ("aguardando cliente ...")

while True  :
    obj_socket.accept()
    conexao , cliente = obj_socket.accept()
    print ("conectado com: " , cliente )

    while True : 
        mensagem = str(conexao.recv(1024))

        print("recebi" , str(mensagem)[2:-1] )
        msg = bytes(input("mensagem : ") , 'utf-8')
        obj_socket.send(msg)
        break
    obj_socket.close()