import serial
import time
import json

# Specify the correct serial port and baud rate
# Replace '/dev/ttyUSB0' with the correct port for your system
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Set a 1-second timeout
time.sleep(2)  # Wait for Arduino to reset

# Open the JSON file in write mode to store the data
file_path = "imu_data.json"  # Specify your file path

# Initialize a list to store data entries
data_list = []

try:
    while True:
        # Check if there's data available in the buffer
        if ser.in_waiting > 0:
            # Read the data from the serial buffer
            data = ser.readline().decode('utf-8').strip()  # Read line and decode to string
            print(data)  # Optionally print to the console
            
            # Create a dictionary for this data entry
            data_entry = {
                "data": data
            }
            
            # Add the data entry to the list
            data_list.append(data_entry)
            
            # Write the updated list to the JSON file after every new entry
            with open(file_path, 'w') as file:
                json.dump(data_list, file, indent=4)
        
        else:
            # No data available, sleep for a short period to prevent high CPU usage
            time.sleep(0.1)  # Sleep for 100ms

except KeyboardInterrupt:
    print("Exiting... Data stored in " + file_path)

finally:
    ser.close()  # Close the serial connection when done

