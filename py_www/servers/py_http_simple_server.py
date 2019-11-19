#!/usr/bin/python3

import logging
import http.server
import ssl

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    log.debug("It works!!")
    try:
        bind_addr = ("localhost", 8000)
        server_handler = http.server.SimpleHTTPRequestHandler

        httpd = http.server.HTTPServer(bind_addr, server_handler)

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