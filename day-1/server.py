import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8000))
server.listen(5)

while True:
    client, addr = server.accept()
    client.sendall(
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: text/html\r\n"
        b"Content-Length: 13\r\n"
        b"\r\n"
        b"Hello, World!"
    )
    client.close()