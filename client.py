
# import the socket module library for TCP connectivity
import socket

IP = '127.0.0.1' # Replace with the desired host (string) to make a connection
PORT = 5000       # Replace with the desired port (number)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT)) #Connect to the server at the specified IP and port
    print(f"[*] Connected to {IP}:{PORT}")
    # Prints the ip address and port the client is connected to

    # Message to send to the server
    client_socket.send(b"That's not true, Ellen. You were invited. Server Connected.")

    # Receive the response from the server
    response = client_socket.recv(1024) # Buffer size is 1024 bytes
    print(f"[*] Received: {response.decode('utf-8')}")
    # Prints the response received from the server

    client_socket.close() # Closes the socket connection

if __name__ == "__main__":
    main() 
    # This will run the main function when the script is executed 
