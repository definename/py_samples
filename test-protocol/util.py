import protocol as proto
import struct


def CalculateChecksum(buff_bytes):
    byte_sum = 0

    for b in buff_bytes:
        byte_sum += b

    return 0xFFFF & -byte_sum


def FindPackets(buff):

    pos_list = list()

    start_code_pos = 0
    buff_size = len(buff)
    while start_code_pos < buff_size - 2:
        # Parse start code
        if struct.unpack(">1H", buff[start_code_pos:start_code_pos + 2])[0] != 0xAA55:
            start_code_pos += 2
            continue

        # Parse frame size
        frame_size_pos = start_code_pos + 2
        frame_size = struct.unpack(">1H", buff[frame_size_pos:frame_size_pos + 2])[0]

        # Parse end code
        end_code_pos = start_code_pos + 6 + frame_size
        if struct.unpack(">1H", buff[end_code_pos:end_code_pos + 2])[0] != 0x0D0A:
            start_code_pos += 2
            continue

        pos_list.append((start_code_pos, end_code_pos + 2))
        start_code_pos += end_code_pos + 2

    return pos_list


def PackFrame(header_dict, frame_data=None):
    if frame_data is None:
        header_dict["data_size"] = 0
    else:
        header_dict["data_size"] = frame_data.size

    frame_header = proto.FrameHeader(**header_dict)
    return proto.FramePacket(frame_header, frame_data)


def PackSerial(frame):
    checksum = CalculateChecksum(bytes(frame))
    return proto.SerialPacket(frame, checksum)


def ParseFrame(frame_bytes):
    header_list = struct.unpack(">3H", frame_bytes[:6])
    frame_header = proto.FrameHeader(*header_list)

    frame_data = None
    if frame_header.data_size != 0:
        frame_data = proto.FrameData(frame_bytes[frame_header.size:])

    return proto.FramePacket(frame_header, frame_data)


def ParseSerial(buff):
    start_code_pos = 0

    # Parse start code
    if struct.unpack(">1H", buff[start_code_pos:start_code_pos + 2])[0] != 0xAA55:
        raise Exception("Invalid start code")

    # Parse frame size
    frame_size_pos = start_code_pos + 2
    frame_size = struct.unpack(">1H", buff[frame_size_pos:frame_size_pos + 2])[0]

    # Parse checksum
    checksum_pos = start_code_pos + 4 + frame_size
    checksum = struct.unpack(">1H", buff[checksum_pos:checksum_pos + 2])[0]

    # Parse end code
    end_code_pos = start_code_pos + 6 + frame_size
    if struct.unpack(">1H", buff[end_code_pos:end_code_pos + 2])[0] != 0x0D0A:
        raise Exception("Invalid end code")

    # Build packets
    frame_pos = start_code_pos + 4
    frame_packet = ParseFrame(buff[frame_pos:frame_pos + frame_size])

    if (CalculateChecksum(bytes(frame_packet)) != checksum):
        raise Exception("Invalid frame checksum")

    serial_packet = proto.SerialPacket(frame_packet, checksum)

    return serial_packet
