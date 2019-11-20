#!/usr/bin/python3

import logging
import http.server
import ssl

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class MyHttpHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        # self.log_message(f"CLIENTADDR:\n{self.client_address}")
        # self.log_message(f"REQUESTLINE:\n{self.requestline}")
        self.log_message(f"HEADERS:\n{type(self.headers)}{self.headers}")
        # self.log_message(f"RESPONSES:\n{type(self.responses)}{self.responses}")
        self.send_response(http.server.HTTPStatus.OK)
        self.send_header("my","header")
        self.end_headers()

    def log_message(self, format, *args):
        log.debug(format, *args)


def main():
    try:
        server_addr = ("", 8000)
        server_handler = MyHttpHandler
        httpd = http.server.HTTPServer(server_addr, server_handler)
        log.debug(f"Socket has been bound on:{server_addr}")

        # keyfile="server_key.key"
        # certfile="server_crt.crt"
        # ca_certs="root_crt.crt"
        # httpd.socket = ssl.wrap_socket(sock=httpd.socket, server_side=True, keyfile=keyfile, certfile=certfile, ca_certs=ca_certs)

        httpd.serve_forever()
    except ssl.SSLError as e:
        log.exception("SSL exception occurred:{e}")
    except KeyboardInterrupt:
        log.debug("Keyboard interupted...")
    except Exception as e:
        log.exception(f"Error occurred:{e}")


if __name__ == "__main__":
    main()