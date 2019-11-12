#!/usr/bin/python3

def calculate_number_of_bit1(x):
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555)
    print(bin(x))
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    print(bin(x))
    x = (x & 0x0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f)
    print(bin(x))
    x = (x & 0x00ff00ff) + ((x >> 8) & 0x00ff00ff)
    print(bin(x))
    x = (x & 0x0000ffff) + ((x >> 16) & 0x0000ffff)
    print(bin(x))
    return x

if __name__ == "__main__":
    x = 15
    print("Result:", calculate_number_of_bit1(x))