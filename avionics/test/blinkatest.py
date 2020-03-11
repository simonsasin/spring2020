import board
import digitalio
import busio

print('Hello blinka!')

#Get digital pin
pin = digitalio.DigitalInOut(board.D4)
print('Digital IO ok!')

#Create i2c device
i2c = busio.I2C(board.SCL, board.SDA)
print('I2C ok!')

#Create SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print('SPI ok!')

print('done')
