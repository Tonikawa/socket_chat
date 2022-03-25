import socket
import threading

HOST = "172.16.38.186"
PORT = 5555

# Instanciando um socket de cone≈ão TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ligando a porta e o IP da conexão à instancia
s.bind((HOST, PORT))
# Colocando o servidor em modo de escuta.
s.listen()

clients = []
nicks = []

# Este método é responsável por enviar mensagens a todos os clients conectados ao chat.
def broadcast(message):
    for client in clients:
        client.send(message)


# Este método trata as mensagens enviadas pelos clientes
def processMessage(client):
    while True:
        try:
            # Aqui a mensagem é recebida e distribuída aos outros clientes pelo método broadcast.
            message = client.recv(1024)
            broadcast(message)
        except:
            # Caso ocorre problema com a conexão e recebimento da mensagem o client é removido da fila de recebimento
            index = clients.index(client)
            clients.remove(client)
            client.close()
            # Aqui avisamos aos outros clients conectados que o alguém foi removido do chat.
            nickname = nicks[index]
            broadcast(f'{nickname} saiu do chat.'.encode('utf-8'))
            nicks.remove(nickname)
            break

# Este é o metodo principal, responsável por receber as mensagens e fazer a chamada dos outros dois métodos.
def receive():
    while True:
        # Enquanto a conexão estiver ativa, o servidor receberá o client e o endereço ip do client
        client, address = s.accept()
        print(f'Conectado com {str(address)}')

        # Assim que estiver conectado, o servidor envia um comando para que o usuário insira um nichname
        # antes de iniciar o chat
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicks.append(nickname)
        clients.append(client)

        print(f'O nickname do cliente é {nickname}')
        broadcast(f'{nickname} entrou no chat!'.encode('utf-8'))
        client.send('\nConectado ao servidor!'.encode('utf-8'))

        # Aqui criamos uma thread para que cada client seja tratado simultaneamente.
        thread = threading.Thread(target=processMessage, args=(client,))
        thread.start()


print("Servidor ativo e escutando...")
receive()

