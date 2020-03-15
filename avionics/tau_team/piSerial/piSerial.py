import serial
import RPi.GPIO as GPIO
import time

port='/dev/ttyAMA0'
baudrate=115200
ser=serial.Serial(port, baudrate)  #change ACM number as found from ls /dev/tty/ACM*
print(ser)
while True:
  read_ser=ser.readline()
  print(read_ser)
  time.sleep(1)
