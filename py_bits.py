import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()


def pack_msg(size, req=True):
    return (0x8000 if req else 0) | size


def unpack_msg(msg):
    is_req = msg & 0x8000
    size = msg & 0x7FFF
    return (is_req, size)


# Origin size
size = 41
log.debug("size: {:016b}".format(size))

# Pack/Unpack request
msg_req = pack_msg(size, req=True)
log.debug("msg_req: {:016b}".format(msg_req))
req_tuple = unpack_msg(msg_req)
log.debug("is_req: {:016b}, size: {:016b}".format(req_tuple[0], req_tuple[1]))

# Pack/Unpack response
msg_resp = pack_msg(size, req=False)
log.debug("msg_resp: {:016b}".format(msg_resp))
resp_tuple = unpack_msg(msg_resp)
log.debug("is_req: {:016b}, size: {:016b}".format(resp_tuple[0], resp_tuple[1]))
