import socket
import sys

# function called from core functionality code.
def scan_target(host):
    ip_host = socket.gethostbyname(host)
    try:
        for port in range(70, 500):
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket object
            socket.setdefaulttimeout(1)
            result = s.connect_ex((ip_host,port))
            if result == 0:
                print(f'{port} is open on {host}')
                s.close()
    except socket.gaierror:
        print("\n hostname couln't be resolved")
        sys.exit()
    except socket.error as err:
        print(err)
        sys.exit()

#core functionality

target = input('Enter the target hostname: ') # could be an ip, ip would make it easier

scan_target(target)