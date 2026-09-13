import serial
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Configuration ---
SERIAL_PORT = 'COM3'  # Change to your Pico's actual USB port
BAUD_RATE = 115200
BASELINE_PRESSURE = 1013.25

# --- Graph Setup ---
# Creates a window with 2 subplots (Temperature on top, Altitude on bottom)
fig, (ax_temp, ax_alt) = plt.subplots(2, 1, figsize=(8, 6))
fig.suptitle('CanSat Live Telemetry')

# Empty lists to hold the graphing data
time_data, temp_data, alt_data = [], [], []

# --- System Setup ---
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
except serial.SerialException:
    print(f"Error connecting to {SERIAL_PORT}. Is the Ground Station plugged in?")
    exit()

filename = f"logs/cansat_flight_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
file = open(filename, mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["Timestamp", "Temperature (C)", "Pressure (hPa)", "Altitude (m)"])
print(f"Connection established! Saving data to {filename}")

# --- The Listener & Graphing Loop ---
def update(frame):
    if ser.in_waiting > 0:
        raw_bytes = ser.readline()
        decoded_string = raw_bytes.decode('utf-8').strip()
        
        if decoded_string:
            data_list = decoded_string.split(',')
            
            # Ensure we didn't receive a half-packet
            if len(data_list) == 2:
                raw_temp = float(data_list[0])
                pressure = float(data_list[1])
                
                # Data Bounds Checking for Temperature (-15 to +60)
                if -15.0 <= raw_temp <= 60.0:
                    temp = raw_temp
                else:
                    temp = -999.0  # Throw the error code if it glitches
                    
                # Calculate Altitude
                if pressure != -999.0:
                    altitude = 44330 * (1 - (pressure / BASELINE_PRESSURE) ** (1 / 5.255))
                else:
                    altitude = -999.0
                    
                current_time = datetime.datetime.now().strftime('%H:%M:%S')
                
                # Log to CSV instantly
                row_to_save = [current_time, f"{temp:.1f}", str(pressure), f"{altitude:.1f}"]
                writer.writerow(row_to_save)
                file.flush() 
                print(f"Received: {row_to_save}")
                
                # --- Update the Graphs ---
                # We only plot valid data; we skip plotting the -999.0 errors
                if temp != -999.0 and altitude != -999.0:
                    time_data.append(current_time)
                    temp_data.append(temp)
                    alt_data.append(altitude)
                    
                    # Keep only the last 20 points so the graph doesn't get squished over time
                    time_data[:] = time_data[-20:]
                    temp_data[:] = temp_data[-20:]
                    alt_data[:] = alt_data[-20:]
                    
                    # Draw Temperature Graph
                    ax_temp.clear()
                    ax_temp.plot(time_data, temp_data, color='red', marker='o')
                    ax_temp.set_title("Temperature (°C)")
                    ax_temp.set_ylim(-15, 60) # Locks the Y-axis to your bounds
                    
                    # Draw Altitude Graph
                    ax_alt.clear()
                    ax_alt.plot(time_data, alt_data, color='blue', marker='o')
                    ax_alt.set_title("Altitude (m)")
                    
                    plt.tight_layout()

# This is the engine that runs the 'update' function every 1000ms (1 second)
ani = animation.FuncAnimation(fig, update, interval=1000)

# Opens the window and starts the loop
plt.show() 

# When you close the graphing window, it safely shuts down the file and port
file.close()
ser.close()
