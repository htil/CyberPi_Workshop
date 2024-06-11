import cyberpi
import time

def read_infrared_obstacle_sensor():
    while True:
        obstacle_detected = cyberpi.pocket.read_digital("s2")
        
        # Clear display before updating the bar chart
        cyberpi.display.clear()
        
        if obstacle_detected == 1:
            cyberpi.console.println("Object Detected")
            cyberpi.display.set_brush(255, 0, 0)  # Set color to red
            cyberpi.barchart.add(20)  # Add a high value to the bar chart for detected
            cyberpi.audio.play("prompt-tone")
        else:
            cyberpi.console.println("Clear")
            cyberpi.display.set_brush(0, 255, 0)  # Set color to green
            cyberpi.barchart.add(1)  # Add a low value to the bar chart for clear
        
        time.sleep(0.5)

read_infrared_obstacle_sensor()
