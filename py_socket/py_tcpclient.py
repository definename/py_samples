#!/usr/bin/python3

import socket
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    try:
        max_size = 1024
        server_address = ("localhost", 6789)

        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.debug(f"TCP client is being connected to:{server_address}")
        tcp_client.connect(server_address)
        tcp_client.sendall(b"Hello")

        data = tcp_client.recv(max_size)
        log.debug(f"Server said:{data.decode()}")
        tcp_client.close()

    except KeyboardInterrupt:
        log.error("Keyboard interrupted...")
    except Exception as e:
        log.error("TCP client error: {}".format(e))
    

if __name__ == "__main__":
    main()