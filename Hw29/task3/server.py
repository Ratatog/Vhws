import threading
import socket
from requests import request
# from api_key import API_KEY

API_KEY = '688c7dea445ed911b2ef69cfc6848c59'
url = 'https://api.openweathermap.org/data/2.5/forecast?q={0}&appid={1}'

clients = {}

def handle_client(client_socket: socket.socket):
    while True:
        header(client_socket, 'Введите город:')
        city = client_socket.recv(1024).decode()
        
        res = request('GET', url.format(city, API_KEY)).json()
        if res['cod'] == '404':
            client_socket.send('\nОшибка: Город не найден\n'.encode())
            continue
        header(client_socket, 'Информация по погоде в городе {city}:')

        weather = res['list'][0]['weather'][0]['main']
        clouds = res['list'][0]['clouds']['all']
        wind_speed = res['list'][0]['wind']['speed']
        msg = f'Погода: {weather}\nОблака: {clouds}\nСкорость ветра: {wind_speed}\n'
        client_socket.send(msg.encode())

        y = ''
        while y.lower() != 'y':
            client_socket.send('\nПродолжить? (y)'.encode())
            y = client_socket.recv(1024).decode()


def header(client_socket: socket.socket, msg):
    msg = '\n\nПолучение данных о погоде:\n\n' + msg
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
        target=handle_client,
        args=(client_socket,)
    )
    client_handler.start()