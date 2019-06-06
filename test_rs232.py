import serial

s = serial.Serial('/dev/ttyUSB0',baudrate=115200)


hexCodes = {
    "on":b"\x0d\x2a\x70\x6f\x77\x3d\x6f\x6e\x23\x0d",
    "off":b"\x0d\x2a\x70\x6f\x77\x3d\x6f\x66\x66\x23\x0d",
   };


def _send_command(k):
    if k in hexCodes:
        for x in hexCodes[k]:
            s.write(x)
    else:
        print('comando non presente non implementato')
