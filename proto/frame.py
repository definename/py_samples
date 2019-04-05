
class FrameHeader:
    def __init__(self, cmd, sub_cmd, error_hash, src_addr, res4, dst_addr, msg, cmd_bit_field, tm_req, proto_v, res10, len_packet):
        self.cmd = cmd
        self.sub_cmd = sub_cmd
        self.error_hash = error_hash
        self.src_addr = src_addr
        self.res4 = res4
        self.dst_addr = dst_addr
        self.msg = msg
        self.cmd_bit_field = cmd_bit_field
        self.tm_req = tm_req
        self.proto_v = proto_v
        self.res10 = res10
        self.len_packet = len_packet

    def __str__(self):
        return "0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x} 0x{:0>4x}".format(
            self.cmd,
            self.sub_cmd,
            self.error_hash,
            self.src_addr,
            self.res4,
            self.dst_addr,
            self.msg,
            self.cmd_bit_field,
            self.tm_req,
            self.proto_v,
            self.res10,
            self.len_packet)