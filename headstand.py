import cyberpi
import time

while True:
    if cyberpi.is_stand():
        cyberpi.led.show('orange')
        cyberpi.console.println("Standing detected!")
        cyberpi.audio.play("yeah")
    elif cyberpi.is_handstand():
        cyberpi.led.show('pink')
        cyberpi.console.println("Handstand detected!")
        cyberpi.audio.play("wow")
    else:
        cyberpi.led.off()
    
    time.sleep(1)
