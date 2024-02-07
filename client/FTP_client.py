import socket

def request_file(file_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 2121))  # Connect to the server

    # Send the requested file name to the server
    client_socket.send(file_name.encode())

    # Receive the file data or error message from the server
    response = client_socket.recv(1024)

    response_str = response.decode()
    print(f"Server response: {response_str}")

    if response_str != "Requested File Not Found" and response_str != "Incorrect File Format":
        with open(file_name, 'wb') as file:
            file.write(response)
            print(f"File '{file_name}' received from the server")

    client_socket.close()

# Ask the user for input
file_name_input = input("Enter the file name: ")

# Example usage
request_file(file_name_input)
