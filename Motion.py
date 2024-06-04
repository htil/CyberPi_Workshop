import cyberpi
import time

motion_threshold = 3.0  

while True:
    motion_value = cyberpi.pocket.read_analog("s2")  
    if motion_value > motion_threshold:
       
        cyberpi.pocket.write_digital(1, "s1")  
        time.sleep(0.5)  
        cyberpi.pocket.write_digital(0, "s1")  
        time.sleep(0.5)  
    else:
        cyberpi.pocket.write_digital(0, "s1")  
    
    cyberpi.console.println(motion_value)  
    time.sleep(1)  
