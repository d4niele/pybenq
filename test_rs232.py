import serial

s = serial.Serial('/dev/ttyUSB1',baudrate=115200)

hexCodes = {
    "on":bytearray('\r*pow=on#\r','ascii'),
    "off":bytearray('\r*pow=off#\r','ascii'),
   };

def _send_command(k):
    if k in hexCodes:
        s.write(hexCodes[k])
    else:
        print('comando non presente non implementato')

def prj_on():
    _send_command('on')

def prj_off():
    _send_command('off')
