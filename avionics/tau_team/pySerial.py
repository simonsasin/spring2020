##################################ISP_Avionics#################################
#        Name: pySerial.py
#     Created: 3.13.20 by Blake Shaffer and Miller McSwain
# Description:

import serial

baudrate = 115200  # set baudrate to 115200 bits/sec
serial_port = "/dev/ttyAMA0"  # UART serial pins PL011


###################################FUNCTIONS!##################################
# -----------------------------------------------------------------------------
# Description:
#          In:
#  Out/Modify:
# -----------------------------------------------------------------------------
def setup_serial():
    piSerial = serial.Serial(serial_port, baudrate)

######################################MAIN#####################################


##################################ISP_Avionics#################################
