#!/usr/bin/python3

import socket
import logging
import threading
import socketserver

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class MyTcpServer(socketserver.TCPServer):

    allow_reuse_address = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__server_thread = None
    
    def server_activate(self):
        log.debug(f"Server is being listened on:{self.server_address}")
        super().server_activate()
    
    def verify_request(self, request, client_address):
        log.debug(f"Client:{client_address} has just connected")
        return True

    def start(self, start_async=True):
        self.server_bind()
        self.server_activate()
        if start_async:
            self.__server_thread = threading.Thread(target=self.serve_forever)
            self.__server_thread.start()
        else:
            self.serve_forever()

    def stop(self):
        self.shutdown()
        self.server_close()
        if self.__server_thread:
            self.__server_thread.join()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

class MyTcpRequestHandler(socketserver.StreamRequestHandler):

    timeout = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        log.debug("Handler has been triggered")
        data = self.rfile.readline()
        if data:
            log.debug(f"Client said:{data.decode()}")
            self.wfile.write("Welcome".encode())


def main():
    try:
        params = {
            "server_address" : ("localhost", 6789),
            "RequestHandlerClass" : MyTcpRequestHandler,
            "bind_and_activate" : False
            }

        tcp_server = MyTcpServer(**params)
        tcp_server.start(False)

    except KeyboardInterrupt:
        tcp_server.stop()
        log.debug("Keyboard interrupted...")
    except Exception as e:
        log.error(f"Error occurred:{e}")


if __name__ == "__main__":
    main()
