import sensor_manager  
import radio_manager 
import time 

# Start the stopwatch before the loop begins
last_transmit_time = time.monotonic()

while True:
    # 1. Instantly check the sensor for new data (never stops)
    readings = sensor_manager.get_readings()     
    
    # 2. Check the current time on the stopwatch
    current_time = time.monotonic()
    
    # 3. If 1 second (1.0) has passed...
    if current_time - last_transmit_time >= 1.0:
        print(readings) # for testing on the ground
        radio_manager.send_data(readings)
        
        # Reset the stopwatch to wait another second
        last_transmit_time = current_time
