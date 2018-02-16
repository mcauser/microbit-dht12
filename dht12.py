"""
MicroPython for micro:bit Aosong DHT12 I2C driver
"""

import time

class DHT12:
    def __init__(self, i2c, address=0x5c):
        self.i2c = i2c
        self.address = address
        self.buf = bytearray(5)
    def measure(self):
        self.i2c.write(0x5c, b'\x00')
        time.sleep_ms(2)
        buf = self.i2c.read(self.address, 5)
        if (buf[0] + buf[1] + buf[2] + buf[3]) & 0xff != buf[4]:
            raise Exception("checksum error")
        self.buf = buf
    def humidity(self):
        return self.buf[0] + self.buf[1] * 0.1
    def temperature(self):
        t = self.buf[2] + (self.buf[3] & 0x7f) * 0.1
        if self.buf[3] & 0x80:
            t = -t
        return t
