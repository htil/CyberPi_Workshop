import cyberpi
import os
import time

def save_file(f_name, content):
    file = open(f_name, 'w')
    # Write some lines of text to the file
    file.write(content)
    # Close the file when done
    file.close()

file_name = "cypi.py"
    
source = """
import cyberpi
import math
import os
import time
import network
import utime
def clear_screen():
    cyberpi.display.clear()
    cyberpi.led.off()
def read_digital(pin="s1"):
    return cyberpi.pocket.read_digital(pin)
    
def read_analog(pin="s1"):
    return cyberpi.pocket.read_analog(pin)
    
def play_tone(freq=2000):
    cyberpi.audio.play_tone(freq)
    stop_audio()
    
def analog_to_celsius(analog_val):
    # analog value from pocket sheid: 0 - 5 volts
    # range for keyestudio lineat temperature sensor 0 - (100 - 200)
    # x = 150 / 5
    max_temp = 200
    max_volts = 5
    x = max_temp / max_volts
    offset = 1.25
    cel =  float(analog_val) * x
    return cel
def analog_to_fahrenheit(val):
    cel = analog_to_celsius(val)
    fah = (cel * (9/5)) + 32
    return fah
def println(msg):
    cyberpi.console.println(msg)
    
def start_new(id):
    cyberpi.display.clear()
    cyberpi.led.off()
    cyberpi.console.println(id)
    play_tone()
    
def stop_audio():
    cyberpi.audio.stop()
    
def read_dir_files(dir):
    # Specify the directory path
    #directory = "/flash"
    
    # Get a list of all files in the directory
    files = [f for f in os.listdir(dir)]
    
    # Print the list of files
    for file in files:
        println(file)
        time.sleep(1)
        
def save_file(f_name, content):
    file = open(f_name, 'w')
    # Write some lines of text to the file
    file.write(content)
    # Close the file when done
    file.close()
    
def read_file():
    file = open('output.txt', 'r')
    file.seek(0)
    lines = file.readlines()
    for line in lines:
        print(line, end='')
    file.close()
    
def wifi_connect(ssid, password):
    cyberpi.led.on(0, 0, 0)
    sta = network.WLAN(network.STA_IF)
    if not sta.isconnected():
        cyberpi.console.println('connecting to network...')
        sta.active(True)
        sta.connect(ssid, password)
        while not sta.isconnected():
            pass
    cyberpi.led.on(0, 100, 0)
    sta = network.WLAN(network.STA_IF)
    info = sta.ifconfig()
    cyberpi.console.println(info)
    
def write_csv(data, filename):
    \"""
    Writes data to a CSV file without using the csv module.
    
    Args:
      data: A list of lists, where each inner list represents a row in the CSV file.
      filename: The filename for the output CSV file.
    \"""
    with open(filename, 'w') as csvfile:
        for row in data:
          # Join elements in each row with a comma as delimiter
          csvfile.write(','.join(map(str, row)) + '\\n')
          
def get_time():
    # Get the current time as a tuple
    current_time = utime.localtime()
    # Extract the hour and minute from the tuple
    hour = current_time[3]
    minute = current_time[4]
    sec = current_time[5]
    return str(hour) + "_" + str(minute) + "_" + str(sec)
"""
    
save_file(file_name, source)
cyberpi.console.println("File Saved.")