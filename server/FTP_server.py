import socket
import os

# Define the directory where files are stored
FILES_DIRECTORY = r"C:\Users\ramis\OneDrive\Desktop\Ramisetty Lakshmi Venkat_CB.EN.U4AIE21152\server"

def handle_client(client_socket):
    # Receive the requested file name from the client
    requested_file = client_socket.recv(1024).decode()

    # Check if the file exists and has a valid extension
    file_path = os.path.join(FILES_DIRECTORY, requested_file)
    if os.path.exists(file_path) and requested_file.endswith('.txt'):
        with open(file_path, 'rb') as file:
            file_data = file.read()
            client_socket.send(file_data)
    else:
        if not os.path.exists(file_path):
            client_socket.send("Requested File Not Found".encode())
        else:
            client_socket.send("Incorrect File Format".encode())

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 2121))  # Set the server to listen on port 2121
    server_socket.listen(5)

    print("Server is listening...")

    while True:
        client, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client(client)

start_server()
