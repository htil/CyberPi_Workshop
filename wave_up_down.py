import cyberpi
import time

while True:
    if cyberpi.is_waveup():
        cyberpi.led.show('green')
        cyberpi.console.println("Wave up detected!")
        cyberpi.audio.play("glass-clink")
    elif cyberpi.is_wavedown():
        cyberpi.led.show('blue')
        cyberpi.console.println("Wave down detected!")
        cyberpi.audio.play("magic")
    else:
        cyberpi.led.off()
    
    time.sleep(1)