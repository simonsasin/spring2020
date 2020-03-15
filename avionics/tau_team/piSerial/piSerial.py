import serial
import time

def read_teensy():
    read_ser=ser.readline()
    print(read_ser)

def write_teensy(msg):
    msg=msg.encode()
    ser.write(msg)

def handshake():
    com_connection=False
    while not(com_connection):
        
        ser.write(b'start')
        read_ser=ser.readline()
        test=str(read_ser)
        print(str(read_ser))
        if len(read_ser)>0:
            com_connection=True
            print('good')

port='/dev/ttyAMA0'
baudrate=115200
ser=serial.Serial(port, baudrate)  #change ACM number as found from ls /dev/tty/ACM*

handshake()
