# 5.20 시리얼 포트와 통신

import serial
ser = serial.Serial('/dev/tty.usbmodem641',  # 디바이스 이름은 달라진다.
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)


ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
