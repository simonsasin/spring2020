import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x

#Configure RFM(x LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
board_created = False
while not board_created:
    #Set up RFM9x Module
    try:
        print('creating board')
        rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
        board_created = True
    except RuntimeError as error:
        print('RFM9x Error:', error)
    
    time.sleep(0.1)
print('RFM9x created')
