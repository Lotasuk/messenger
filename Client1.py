import socket
from _thread import *

def listen(con):
    try:
        while True:
            data = con.recv(1024)
            message = data.decode()
            if (len(message) == 0):
                con.close()
            else:
                print(f"{message}")
    except:
        con.close()

def send(con):
    try:
        while True:
            message = input(": ")
            con.send(message.encode())
    except Exception as e:
        con.close()
        print(f"Except close = {e}")
    con.close()
    print("Cycle end close")


client = socket.socket()            # создаем сокет клиента
hostname = socket.gethostname()     # получаем хост локальной машины
port = 12345
client.connect((hostname, port))    # подключаемся к серверу

start_new_thread(listen, (client,))
start_new_thread(send, (client,))
print("Line end close")
while True:
    a = 1