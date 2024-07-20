import threading
import socket
import time


clients = {}
ready_count = 0

def handle_new_connection(client_socket: socket.socket):
    global ready_count
    if len(clients) == 2:
        client_socket.send('Неудача подключения. Комната заполнена'.encode())
        client_socket.close()
        return
    
    # client_socket.send('Введите ник:'.encode())
    username = client_socket.recv(1024).decode()
    clients[username] = client_socket

    send_message(f'Подключен игрок: {username}', username)
    client_socket.send('Добро пожаловать! Введите любое сообщение для старта'.encode())
    client_socket.recv(1024).decode()
    ready_count += 1

    send_message(f'Игроков готово: {ready_count}')
    while True:
        if ready_count == 2:
            handle_client(client_socket)
            break


def handle_client(client_socket: socket.socket):
    global ready_count
    while True:
        try:
            client_socket.send('Процесс игры...'.encode())
            time.sleep(1)
        except Exception:
            break

    client_socket.close()
    ready_count -= 1

def send_message(msg, username=None):
    for c in clients.keys():
        if c != username:
            clients[c].send(msg.encode())


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