# import the socket module library for TCP connectivity
import socket
# import the threading module to handle multiple clients simultaneously
import threading

IP = '0.0.0.0'  # Listen on all interfaces
PORT = 5000 # Port to listen on

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT)) # Binds the socket to the specified IP and port
    server_socket.listen(5)  # Listen for incoming connections
    print(f'[*] Listening on {IP}:{PORT}') # Prints the listening ip address and port


    while True:
        client_socket, addr = server_socket.accept() # Accepts a connection from a client
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')
        # Prints the address of the client that connected
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        # Starts a new thread to handle the client
        client_handler.start() # Starts the client handler thread

def handle_client(client_socket): # Handles the client connection
    with client_socket as sock:
        request = sock.recv(1024) # Receives data from the client
        print(f'[*] Received: {request.decode("utf-8")}')
        # Prints the data received from the client
        sock.send(b'ACK')  # Sends an acknowledgment back to the client
        print('[*] Sent: ACK')
        # Prints the acknowledgment sent to the client

if __name__ == '__main__':
    main() # Calls the main function to start the server

