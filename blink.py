# D Wilson June 2016 (original work 2014)

import time
import json
import sys
 
def pins_export():
	try:
		pin1export = open("/sys/class/gpio/export","w")
		pin1export.write("39")
		pin1export.close()
	except IOError:
		print "INFO: GPIO 39 already exists, skipping export"

	fp1 = open( "/sys/class/gpio/gpio39/direction", "w" )
	fp1.write( "out" )
	fp1 = open( "/sys/class/gpio/gpio39/value", "w" )
	fp1.close()
	#fp1.write( "0" )

def write_led( value ):
	fp2 = open( "/sys/class/gpio/gpio39/value", "w" )
	fp2.write( str( value ) )
	fp2.close()

pins_export()


while (1):
	write_led(1)
	print "hi"
	time.sleep(20)
	write_led(0)
	print "low"
	time.sleep(3) 
