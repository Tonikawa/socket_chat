import socket
import sys

HOST = "172.16.38.186"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

done = False

print("Digite QUIT para encerrar o chat.")

while not done:
    client.send(input("Mensagem: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == "QUIT":
        done = True
        client.send("QUIT".encode('utf-8'))
        break
    else:
        print(msg)
client.close()
sys.exit()


