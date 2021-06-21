import serial

ser = serial.Serial("COM1", 115200)
while True:
    tex = 'a'
    ser.write(tex.encode())
