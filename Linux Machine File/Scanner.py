#!/bin/python3

import sys
import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    try:
        # Add a pretty banner
        print("-" * 50)
        print("Scanning target " + target)
        print("Time started: " + str(datetime.now()))
        print("-" * 50)

        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))  # returns an error indicator - if port is open it throws a 0, otherwise 1
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    except socket.error:
        print("Could not connect to server.")
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Invalid amount of arguments.")
        print("Syntax: python3 scanner.py <target> <start_port> <end_port>")
        sys.exit()

    target = socket.gethostbyname(sys.argv[1])
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    scan_ports(target, start_port, end_port)
