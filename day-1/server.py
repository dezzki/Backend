import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8808))
server.listen(5)

while True:
    client, addr = server.accept()
    client.sendall(b'Hello, World!')
    client.close()