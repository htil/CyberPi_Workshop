import cyberpi
import time

while True:
    if cyberpi.is_tiltforward():
        cyberpi.led.show('green')
        cyberpi.console.println("Tilted forward detected!")
        cyberpi.audio.play("right")
    elif cyberpi.is_tiltback():
        cyberpi.led.show('blue')
        cyberpi.console.println("Tilted backward detected!")
        cyberpi.audio.play("wrong")
    else:
        cyberpi.led.off()
    
    time.sleep(1)