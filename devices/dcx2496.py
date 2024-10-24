import serial
import logging

class DCX2496:
    def __init__(self, port:str, device_id: bytes):
        logging.basicConfig(level=logging.DEBUG)
        self.device_id = device_id
        #self.s = serial.Serial(port=port, baudrate=38400)
        self.send_serial(b"\x3f",b"\x04\x00")

    def set_gain(self, gain):
        pass

    def send_serial(self, fn: bytes, value: bytes):
        buffer = b''.join([b"\xf0\x00\x20\x32", self.device_id, b"\x0e", fn, value, b"\xf7"])
        logging.debug("Sending following buffer: " + buffer.hex())
        #self.s.write(buffer)