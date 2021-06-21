import serial

ser = serial.Serial("COM2", 115200)
while True:
    cc = str(ser.readline())
    if cc:
        print('1')
    # print(cc[2:][:-5])
