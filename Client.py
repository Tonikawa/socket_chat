import socket
import threading

HOST = "172.16.38.186"
PORT = 5555

nickname = input("Escolha um Nick para participar do chat: ")

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((HOST, PORT))

# Esta função roda constantemente e é responsável por receber mensagens do servidor
def receive():
    while True:
        try:
            message = cli.recv(1024).decode('utf-8')
            if message == 'NICK':
                cli.send(nickname.encode('utf-8'))
                pass
            else:
                print(message)
        except:
            print("Ocorreu um erro!")
            cli.close()
            break

# Esta função roda constantemente e fica aguardadndo pelo input do client.
def write():
    while True:
        message = f'{nickname}: {input("")}'
        cli.send(message.encode('utf-8'))


# Aqui iniciamos as threads respinsáveis por fazer nossos métodos rodarem simultaneamente.
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()






