import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x

#Configure the RFM9x LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None
count = 0
while True:
    count += 1
    packet = rfm9x.receive()
    if packet is None:
        print('Waiting for packet')
    else:
        print("Packet recieved", "utf-8", count)
    time.sleep(0.1)
    
