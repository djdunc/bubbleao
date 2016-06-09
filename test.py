import mraa    
import time    
    
# This is a simple light switch code    
# connect Touch Sensor to the D4 and the Relay to the D8    
    
# inside a python interupt you cannot use 'basic' types so you'll need to use objects    
class Toggle:    
  state = 0    
    
t=Toggle()    
    
# D8 for the relay    
mraa.Gpio(8).dir(mraa.DIR_OUT)    
    
# D4 for the touch sensor    
mraa.Gpio(4).dir(mraa.DIR_IN)    
    
def pressed(args):    
  if t.state==0:    
    mraa.Gpio(8).write(1)    
    t.state = 1    
  else:    
    mraa.Gpio(8).write(0)    
    t.state = 0    
    
# here the interrupt is set on Gpio(4)    
# fourth argument is not used    
mraa.Gpio(4).isr(mraa.EDGE_RISING, pressed, pressed)    
    
# Delay destructors on script termination otherwise ISR will not run    
time.sleep(60) 