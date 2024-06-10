import cyberpi
import time

def display_vibration_readings():
    # Define the vibration threshold (analog reading)
    threshold = 0.04  
    while True:
        vibration_value = cyberpi.pocket.read_analog("s2")  
        if vibration_value > threshold:
            # Play a sound when vibration is detected
            cyberpi.audio.play_tone(1000, 0.5) 
            cyberpi.console.println("Vibration!", )
        else:
            cyberpi.console.println("No Vibration.")
        time.sleep(0.5)  

display_vibration_readings()
