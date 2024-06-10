import cyberpi
import time

def button_hold_time():
    while True:
        cyberpi.console.println("Hold the Button...")
        cyberpi.led.on('green')
        while cyberpi.pocket.read_digital("s2") == 1:
            pass
        start_time = time.time()
        cyberpi.console.println("Release the Button!")
        cyberpi.led.on('red')
        
        while cyberpi.pocket.read_digital("s2") == 0:
            time.sleep(1)
        
        hold_time = time.time() - start_time
        cyberpi.console.println(f"Hold Time: {hold_time:.3f} seconds")
        cyberpi.led.off()
        time.sleep(3)

button_hold_time()
