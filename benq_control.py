from flask import Flask
import serial

s = serial.Serial('/dev/ttyUSB0',baudrate=115200)

hexCodes = {
    "on":bytearray('\r*pow=on#\r','ascii'),
    "off":bytearray('\r*pow=off#\r','ascii'),
   }

def _send_command(k):
    if k in hexCodes:
        s.write(hexCodes[k])
    else:
        print('comando non presente non implementato')

def prj_on():
    _send_command('on')

def prj_off():
    _send_command('off')

app = Flask(__name__)

@app.route("/benq_off")
def benq_off():
    prj_off()    
    return 'ok'

@app.route("/benq_on")
def benq_on():
    prj_on()    
    return 'ok'

if __name__ == "__main__":
    app.run('0.0.0.0')
