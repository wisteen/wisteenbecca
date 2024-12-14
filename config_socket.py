import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
server_address = ('localhost', 8080)  # Use the desired port
server_socket.bind(server_address)

# Enable the server to listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")
while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")
        data = connection.recv(1024)
        print(f"Received: {data.decode()}")
        connection.sendall(b'HTTP/1.1 200 OK\n\nHello, World!')
    finally:
        connection.close()
