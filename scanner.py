import serial
import logging

logging.basicConfig(filename='events.log', filemode='w', format='%(asctime)s:%(message)s', level=logging.DEBUG)

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

while True:
    line = ser.readline()
    if len(line)>8:
        logging.info(line)

