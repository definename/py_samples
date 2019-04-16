import protocol as proto
import util
import struct
import socket
import logging
import time

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("CLIENT")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

max_size = 1024
addr = ("localhost", 6789)


def main():
    # Build frame
    frame_data = proto.FrameData(struct.pack(">10B", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    logger.debug("Data: {} size: {}".format(bytes(frame_data), frame_data.size))

    header_dict = {
        "command": 0x0001,
        "version": 0x0002
    }

    frame_packet = util.PackFrame(header_dict, frame_data)
    # frame_packet = util.PackFrame(header_dict)
    logger.debug("Frame packet: {} size: {}".format(bytes(frame_packet), frame_packet.size))

    # Build serial
    serial_packet = util.PackSerial(frame_packet)
    logger.debug("Serial packet: {} size: {}".format(bytes(serial_packet), serial_packet.size))
    logger.debug("Serial checksum: {}".format(serial_packet.checksum))

    # Send
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            try:
                client.connect(addr)

                while True:
                    logger.debug("Send serial packet")
                    data = b"".join([bytes(serial_packet), bytes(serial_packet)])
                    client.sendall(data)
                    time.sleep(5)

            except Exception as e:
                logger.debug("Socket error occurred: {}".format(e))
                time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.debug("Protocol client error: {}".format(e))
