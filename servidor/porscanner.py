import socket 
import os

os.system("cls")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('bancocn.com', 80 ))
client.send(b"oi mundo")

resposta = client.recv(1024)
print(resposta.decode())