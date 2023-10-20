import socket
from _thread import *


# функция для обработки каждого клиента
def client_thread(con):
    try:
        message = "Enter your name: "
        con.send(message.encode())
        data = con.recv(1024)
        name = data.decode()
        message = f"Welcome, {name}!"
        con.send(message.encode())
        print(message)
        while True:
            data = con.recv(1024)
            message = data.decode()
            print(f"{name} sent: {message}")
            for i in clients:
                if i != con:
                    i.send(f"{name} sent: {message}".encode())
    except Exception as e:
        con.close()
        print(f"Server except close = {e}")


server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12345  # устанавливаем порт сервера
server.bind((hostname, port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений

clients = []

print("Server running")
while True:
    client, _ = server.accept()  # принимаем клиента
    clients.append(client)
    start_new_thread(client_thread, (client,))  # запускаем поток клиента
