#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
	n = 0
	temp0 = 0
	temp1 = 0
	temp2 = 0
	while n<4:
		n = n + 1
       		x = ser.readline()
        	temp0 = temp0 + float(x.split(";")[0])
		temp1 = temp1 + float(x.split(";")[1])
		temp2 = temp2 + float(x.split(";")[2])
	temp0 = temp0/4
	
	temp1 = temp1/4
	temp2 = temp2/4

	if temp0 < 27:
		print "No figure"
	elif 27 <= temp0 < 50:
		print "Pawn"
		print temp0 
	elif 50 <= temp0 < 70:
       		print "Rook"
		print temp0
	elif 70 <= temp0 < 90: 
	        print "King" 
		print temp0
	else:
		print "No result"
		print temp0
	

