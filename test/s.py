import serial
import time

from obdi import OBDI

ob = OBDI()
print ob.set_cmd("010D")


ser = serial.Serial('/dev/rfcomm0', baudrate=38400, timeout=1)
print ser.name

while True:
	ser.write("01 0D\r")
	speed = ser.readline().split(' ')
        speed = speed[len(speed)-2]
        if speed != '':
            print "speed: ", float(int('0x'+ speed, 0))

	#ser.write("01 0C\r")
	#rpm = ser.readline().split(' ')
	#ser.write("01 05\r")
	#temp = ser.readline().split(' ')
	#ser.write("01 11\r")
	#tp = ser.readline().split(' ')
	#print float(int('0x' + speed[2], 0))*0.6214, float(int('0x' + (rpm[2]+rpm[3]), 0)), \
	# float(int('0x' + temp[2], 0)), float(int('0x' + tp[2], 0))
	#time.sleep(0.1)
ser.close()
