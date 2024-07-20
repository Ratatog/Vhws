import threading
import socket


def receive_message(client_socket: socket.socket):
    while True:
        try:
            message = client_socket.recv(4096).decode()
        except Exception:
            break
        print(message)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8000
client_socket.connect((host, port))

username = input('Введите ваш ник:\n-->')
client_socket.send(username.encode())

receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
receive_thread.start()

while True:
    message = input()
    client_socket.send(message.encode())
    if 1 == 2:
        break

client_socket.close()