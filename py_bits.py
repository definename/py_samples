import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()


def pack_msg(size, req=True): return (0x8000 if req else 0) | size


def is_req(msg): return msg & 0x8000


def unpack_size(msg): return msg & 0x7FFF


# Origin size
size = 41
log.debug("size: {:016b}".format(size))

# Pack/Unpack request
msg_req = pack_msg(size, req=True)
log.debug("msg_req: {:016b}".format(msg_req))
log.debug("is_req: {:016b}".format(is_req(msg_req)))
log.debug("size: {:016b}".format(unpack_size(msg_req)))

# Pack/Unpack response
msg_resp = pack_msg(size, req=False)
log.debug("msg_resp: {:016b}".format(msg_resp))
log.debug("is_req: {:016b}".format(is_req(msg_resp)))
log.debug("size: {:016b}".format(unpack_size(msg_resp)))
