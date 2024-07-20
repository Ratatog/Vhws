import threading
import socket
import time


clients = {}

def handle_new_connection(client_socket: socket.socket):
    username = client_socket.recv(1024).decode()
    clients[username] = client_socket

    handle_client(client_socket, username)


def handle_client(client_socket: socket.socket, username):
    while True:
        if username not in clients:
            transfering(sender=False)

        print_users()
        choice = client_socket.recv(1024).decode()
        if not (choice.isalnum() and 1 <= int(choice) <= len(clients)):
            continue

        choice = int(choice)
        i = 0
        for k in clients.keys():
            if k == username: continue
            i += 1
            if i == choice:
                c1 = clients.pop(username)
                c2 = clients.pop(k)
                transfering(c1, c2)

def transfering(client1=None, client2=None, sender=True):
    print_users()
    if not sender:
        while True:
            time.sleep(1)
    else:
        while True:
            client1.send('Процесс обмена...'.encode())
            client2.send('Процесс обмена...'.encode())
            time.sleep(1)


def print_users():
    print(clients)
    for username, client_socket in clients.items():
        msg = '\n'*50 + 'Активные пользователи:\n'
        i = 0
        for c in clients.keys():
            if c == username: continue
            i += 1
            msg += f'{i}. {c}\n'
        msg += f'{len(clients)}. Обновить\n-->\n'
    
        client_socket.send(msg.encode())
    


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8000
server_socket.bind((host, port))
server_socket.listen()

print(f'Servers starting listening on port {port}')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')

    client_handler = threading.Thread(
        target=handle_new_connection,
        args=(client_socket,)
    )
    client_handler.start()