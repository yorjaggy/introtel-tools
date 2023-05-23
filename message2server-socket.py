import socket

HOST = 'localhost'
PORT = 2335
message2send = input('ingrese el mensaje a enviar:')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f'Sending msg: {message2send}')
    s.connect((HOST, PORT))
    s.sendall(str.encode(message2send))
    data = s.recv(1024)

print('Received:', data.decode())
