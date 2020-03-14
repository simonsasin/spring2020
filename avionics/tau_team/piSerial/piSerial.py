##################################ISP_Avionics#################################
#        Name: pySerial.py
#     Created: 3.13.20 by Blake Shaffer and Miller McSwain
# Description:

import serial

baudrate = 115200  # set baudrate to 115200 bits/sec
serial_port = "/dev/ttyS0"  # UART serial pins PL011


###################################FUNCTIONS!##################################
# -----------------------------------------------------------------------------
# Description:
#          In:
#  Out/Modify:
# -----------------------------------------------------------------------------
ser = serial.Serial(serial_port, baudrate)


i=0
while True:
    print(i)

    ser.write(b"hi from pi")
    read_ser=ser.readline()
    print(read_ser)
    i=i+1
######################################MAIN#####################################


##################################ISP_Avionics#################################
