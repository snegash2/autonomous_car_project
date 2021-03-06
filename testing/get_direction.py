import smbus
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_I2C import Adafruit_I2C

def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val 

def get_direction():
	GPIO.setup("P8_10", GPIO.IN)
	#read adress 0x3D
	bus = Adafruit_I2C(address=0x1E)
	#check if dready is high
	if GPIO.input("P8_10"):
		x1=bus.readU8(3)
		x2=bus.readU8(4)
		mode=bus.readU8(2)
		if bus.readU8(2)!=0:
			print mode
			x1=bus.write8(2, 0)
		#register address (in hex)
		#03 msb of x
		#04 lsb
		#07 msb of y
		#08 lsb
		
		#print bus.readU8(0)
		#print bus.readU8(1)
		#print bus.readU8(2)
		#print bus.readU8(9)
		
		x1=bus.readU8(3)
		x2=bus.readU8(4)
		z1=bus.readU8(5)
		z2=bus.readU8(6)
		y1=bus.readU8(7)
		y2=bus.readU8(8)
		#to binary
		x1_conc_x2 = (x1<<8)| (x2)
		y1_conc_y2 = y1<<8| (y2)
		#concatenate
		
		#2's complement
		print twos_comp(x1_conc_x2, 16)
		print twos_comp(y1_conc_y2, 16)
		print x1,x2
		print y1,y2
		print z1,z2
		#concatanate and convert to float.
		return 0

	else:
		print 'compass not ready'
		return 1
if __name__ == "__main__":
	print get_direction()	
	#while(get_direction()):
	#	pass
