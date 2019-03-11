
bList = [1, 2, 3, 255]
theBytes = bytes(bList)
print("{}".format(theBytes))

theByteArray = bytearray(bList)
print("{}".format(theByteArray))

theByteArray[0] = 127
print("{}".format(theByteArray))

a = 10
print(a << 1)
print(a >> 1)