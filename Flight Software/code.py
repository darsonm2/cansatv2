import sensor_manager 
import radio_manager
import time

while True:
    readings = sensor_manager.get_readings()
    print(readings) # for testing 
    radio_manager.send_data(readings)
    time.sleep(1) # adjust it as needed