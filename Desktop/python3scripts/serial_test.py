import serial
from time import sleep

# plug in ESP32 to top right of RPi

sr = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.02
        )
i = 0
while True:
    #i += 1
    x = sr.readline()
    if x:
        byte_to_str = x.decode('utf-8')
        print(byte_to_str)
        
    #print("test " + str(i) + ": " + byte_to_str)
    #print(x)
    
    sleep(0.02)