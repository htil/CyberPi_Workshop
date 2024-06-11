import cyberpi
import time

while True:
    if cyberpi.is_freefall():
        cyberpi.led.show('red')
        cyberpi.console.println("Free fall detected!")
        cyberpi.audio.play("laser")
    else:
        cyberpi.led.off()
    
    time.sleep(.5)
