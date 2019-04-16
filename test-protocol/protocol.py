import struct


class Measurable:
    @property
    def size(self):
        return len(bytes(self))


class FrameHeader(Measurable):
    def __init__(self, command, version, data_size):
        self.command = command
        self.version = version
        self.data_size = data_size
        self.mngr = struct.Struct(">3H")

    def __str__(self):
        return """
            command: {}
            version: {}
          data_size: {}""".format(self.command,
                                  self.version,
                                  self.data_size)

    def __bytes__(self):
        return self.mngr.pack(self.command,
                              self.version,
                              self.data_size)


class FrameData(Measurable):
    def __init__(self, payload_bytes):
        self.__payload_bytes = payload_bytes

    def __bytes__(self):
        return self.__payload_bytes


class FramePacket(Measurable):
    def __init__(self, frame_header, frame_data=None):
        self.__frame_header = frame_header
        self.__frame_data = frame_data

    def __bytes__(self):
        if self.__frame_data is None:
            return b"".join([bytes(self.__frame_header)])
        else:
            return b"".join([bytes(self.__frame_header), bytes(self.__frame_data)])

    @property
    def header(self):
        return self.__frame_header

    @property
    def data(self):
        return self.__frame_data


class SerialPacket(Measurable):
    def __init__(self, frame, checksum):
        self.__start_code = 0xAA55
        self.__frame = frame
        self.__checksum = checksum
        self.__end_code = 0x0D0A

    def __bytes__(self):
        mngr = struct.Struct(">1H")
        return b"".join([
            mngr.pack(self.__start_code),
            mngr.pack(self.__frame.size),
            bytes(self.__frame),
            mngr.pack(self.__checksum),
            mngr.pack(self.__end_code)])

    @property
    def frame(self):
        return self.__frame

    @property
    def checksum(self):
        return self.__checksum
