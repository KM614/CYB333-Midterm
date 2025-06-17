# import the socket module library for TCP connectivity
import socket
# from utils import timefunc measures the time it takes to perform a function.
from utils import timefunc


# Building Scanner as a class allows you to cache an ip as an object
# so you can use it later without passing it around as a parameter.

class Scanner:
    def __init__(self, IP):
        # self.ip assigns the ip address to the Scanner object
        self.IP = IP
        # self.open_ports is a list that will hold the open ports found during the scan.
        self.open_ports = [];

# __repr__ is a method that defines how the object is represented.
    def __repr__(self): 
        return 'Scanner: {}'.format(self.IP)
    
    
    def add_port(self, port):
        self.open_ports.append(port)


    def scan(self, lowerport, upperport):
        # This method scans the range of ports from the lowerport to upperport
        # to include +1 for the upper port.
        for port in range(lowerport, upperport + 1):
            # It calls the is_open method to check if the port is open.
            if self.is_open(port):
                # If the port is open, it appends the port to the open_ports list.
                self.add_port(port)

# def is_open tests the connectivity of a port on the ip address.
    def is_open(self, port):

        # 's' is a standard TCP socket object used to connect to the port.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # s.settimeout(0.1) sets a timeout of 0.1 seconds for the connection attempt.
        # any timeout shorter than 0.1 seconds will not allow 
        # enough time for the connection to be established.
        s.settimeout(0.1)

        result = s.connect_ex((self.IP, port))
# If the result is 0, it means the port is open.
# If the result is not 0, it means the port is closed or unavaliable.

        print('Port {}:      {}'.format(port, result))
        s.close()
        # s.close() closes the socket connection.

        return result == 0
    # return result == 0 returns True if the port is open, otherwise False.

# def write(self, filepath) takes a filepath and outputs the results
# of the scan to a file.
    def write(self, filepath):
        openport = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(openport))

@timefunc
def main():
    IP = 'scanme.nmap.org'
    scanner = Scanner(IP)
    scanner.scan(1, 1024)
    print(scanner.open_ports)
    scanner.write('./open_ports.txt')
    # This line will perform a port scan, print the open ports,
    # and write the results to a file named 'open_ports.txt'.

# This script designates the port scanner to be run as a standalone program.
if __name__ == '__main__':
    main()