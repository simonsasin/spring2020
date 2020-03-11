import time
import busio
from digitalio import DigitalInOut
import board
import adafruit_rfm9x

#Configure the RFM9x LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None

while True:
    packet_data=bytes('Packet sent', "utf-8")
    rfm9x.send(packet_data)
    print('packet sent')
    time.sleep(0.1)


