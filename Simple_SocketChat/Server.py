import socket

HOST = "172.16.38.186"
PORT = 320907

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

client, address = server.accept()
print(f'Conectado com {str(address)}')

done = False

while not done :
   # client.send('Conectado ao servidor!'.encode('utf-8'))
    message = client.recv(1024).decode('utf-8')
    if message == "QUIT":
        done = True
        client.send("QUIT".encode('utf-8'))
    else:
        print(message)
        client.send(input("Mensagem: ").encode('utf-8'))

client.close()
server.close()
