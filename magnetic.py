import cyberpi
import time

def read_magnetic_sensor():
    while True:
        magnetic_value = cyberpi.pocket.read_digital("s2")  
        if magnetic_value == 0:
            cyberpi.console.println("Magnet Detected")
            cyberpi.led.on("blue")  
            cyberpi.audio.play("prompt-tone")  
        else:
            cyberpi.console.println("No Magnet Detected")
            cyberpi.led.off()  
        
        time.sleep(1)  

read_magnetic_sensor()
