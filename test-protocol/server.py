import logging
import threading
import socket
import time
import struct
import protocol as proto
import util

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("SERVER")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

max_size = 1024
addr = ("localhost", 6789)

client_list = list()


def ServerHandler(server):
    server.bind(addr)
    server.listen(5)

    try:
        while True:
            logger.debug("Accept incoming connection on {}".format(addr))

            client, client_addr = server.accept()
            client_list.append(client)

            logger.debug("Accepted incoming connection {}".format(client_addr))

            while True:
                buff = client.recv(max_size)
                logger.debug("Client: {} sent: {} bytes\n".format(client_addr, len(buff)))

                try:
                    pos_list = util.FindPackets(buff)

                    for start, end in pos_list:

                        logger.debug("start {}, end {}".format(start, end))

                        # Serial
                        serial_packet = util.ParseSerial(buff[start:end])
                        logger.debug("Checksum {}".format(serial_packet.checksum))

                        # Frame
                        frame_packet = serial_packet.frame

                        # Frame header
                        frame_header = frame_packet.header
                        logger.debug("Frame header: {}".format(frame_header))

                        # Deserialize frame data.
                        if not frame_packet.data is None:
                            frame_data = frame_packet.data
                            data_fmt = ">{}B".format(frame_header.data_size)
                            logger.debug("Frame data: {}".format(
                                struct.unpack(data_fmt, bytes(frame_data))))

                except Exception as e:
                    logger.error("Failed to unpack received buff: {}".format(e))

                if not buff:
                    logger.debug("Release client socket {}".format(client_addr))
                    client.close()

                    break

    except Exception as e:
        logger.error("Server handler error: {}".format(e))


desc = """Usage:
    'q' - exit;
    '?' - get this help.
"""


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    thread = threading.Thread(target=ServerHandler, args=(server, ))
    thread.start()

    while True:
        val = input(desc)
        if val == "q":
            server.close()

            for c in client_list:
                c.close()

            break
        elif val == "?":
            logging.debug(desc)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error("Protocol server error: {}".format(e))
