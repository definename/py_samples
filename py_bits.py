import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()


class Header():
    @staticmethod
    def pack_msg(num, req=True): return (0x8000 if req else 0) | num

    @staticmethod
    def is_msg_req(msg): return msg & 0x8000

    @staticmethod
    def get_msg_num(msg): return msg & 0x7FFF

    @staticmethod
    def reset_msg_req_bit(msg):
        return msg ^ 0x8000


def line(): return log.debug("{:=^100s}".format("Line"))


# Origin num
num = 41
log.debug("num: {:016b}".format(num))

# Pack/Unpack request
msg_req = Header.pack_msg(num, req=True)
log.debug("msg_req: {:016b}".format(msg_req))
log.debug("is_msg_req: {:016b}".format(Header.is_msg_req(msg_req)))
log.debug("num: {:016b}".format(Header.get_msg_num(msg_req)))

line()

# Pack/Unpack response
msg_resp = Header.pack_msg(num, req=False)
log.debug("msg_resp: {:016b}".format(msg_resp))
log.debug("is_msg_req: {:016b}".format(Header.is_msg_req(msg_resp)))
log.debug("num: {:016b}".format(Header.get_msg_num(msg_resp)))

line()

log.debug("reset req bit: {:016b}".format(Header.reset_msg_req_bit(msg_req)))
log.debug("reset resp bit: {:016b}".format(Header.reset_msg_req_bit(msg_resp)))
