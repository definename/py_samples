import unittest
import util
import struct


class Test_Protocol(unittest.TestCase):
    def setUp(self):
        self.serial_bytes = bytes.fromhex("aa55001000010002000a00010203040506070809ffc60d0a")
        self.size = len(self.serial_bytes)
        self.checksum = struct.unpack(">1H", self.serial_bytes[self.size - 4:self.size - 2])[0]
        self.frame_bytes = self.serial_bytes[4:self.size - 4]

    def tearDown(self):
        pass

    def test_checksum_calculation(self):
        self.assertEqual(util.CalculateChecksum(self.frame_bytes), self.checksum)

    def test_serial_parsing(self):
        serial = util.ParseSerial(self.serial_bytes)
        self.assertEqual(serial.checksum, self.checksum)

        frame = serial.frame
        self.assertEqual(frame.header.data_size, 10)
        self.assertEqual(frame.data.size, 10)


if __name__ == "__main__":
    unittest.main()
