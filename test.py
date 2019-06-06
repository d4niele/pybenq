import serial

s = serial.Serial('/dev/ttyUSB0',baudrate=115200)


hexCodes = {"on":[0x0d, 0x2a, 0x70, 0x6f, 0x77, 0x3d, 0x6f, 0x6e, 0x23, 0x0d],
    "off":[0x0d, 0x2a, 0x70, 0x6f, 0x77, 0x3d, 0x6f, 0x66, 0x66, 0x23, 0x0d],
    "video":[0x0d, 0x2a, 0x73, 0x6f, 0x75, 0x72, 0x3d, 0x76, 0x69, 0x64, 0x23, 0x0d],
    "hdmi-1":[0x0d, 0x2a, 0x73, 0x6f, 0x75, 0x72, 0x3d, 0x68, 0x64, 0x6d, 0x69, 0x23, 0x0d],
    "hdmi-2":[0x0d, 0x2a, 0x73, 0x6f, 0x75, 0x72, 0x3d, 0x68, 0x64, 0x6d, 0x69, 0x32,0x23, 0x0d],
    "pc":[0x0d, 0x2a, 0x73, 0x6f, 0x75, 0x72, 0x3d, 0x52, 0x47, 0x42, 0x23, 0x0d],
   };


def send_command(k):
    if k in hexCodes:
        for x in hexCodes[k]:
            s.write(x)
    else:
        print('codice non presente')
