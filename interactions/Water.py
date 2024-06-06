import cyberpi
import time

water_threshold = 2.0

while True:
    state_s2_vol = cyberpi.pocket.read_analog("s2")
    state_s2_vol = float(state_s2_vol)
    if state_s2_vol > water_threshold:
        cyberpi.pocket.write_digital(1, "s1")  
    else:
        cyberpi.pocket.write_digital(0, "s1")  
    
    cyberpi.console.println(state_s2_vol)
    time.sleep(1)  
