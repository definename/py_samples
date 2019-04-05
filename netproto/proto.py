import logging

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("netproto")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

import struct
import frame

def main():

    outf = frame.FrameHeader(0x0001, 0x0002, 0x0003, 0x0004, 0x0005, 0x0006, 0x0007, 0x0008, 0x0009, 0x0010, 0x0011, 0x0012)
    logger.debug("Origin frame header: {}".format(outf))

    header = struct.Struct(">12H")

    out_data = header.pack(outf.cmd, outf.sub_cmd, outf.error_hash, outf.src_addr, outf.res4, outf.dst_addr, outf.msg, outf.cmd_bit_field, outf.tm_req, outf.proto_v, outf.res10, outf.len_packet)
    logger.debug("{} {}".format(out_data, type(out_data)))

    in_data = header.unpack(out_data)
    logger.debug("{} {}".format(in_data, type(in_data)))

    inf = frame.FrameHeader(*in_data)
    logger.debug("Parsed frame header: {}".format(inf))


if __name__ == "__main__":
    main()