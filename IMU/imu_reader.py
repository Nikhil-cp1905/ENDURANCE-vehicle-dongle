import serial
import time

# Specify the correct serial port and baud rate
# Replace '/dev/ttyUSB0' with the correct port for your system
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Set a 1-second timeout
time.sleep(2)  # Wait for Arduino to reset

# Read and print data from the Arduino
try:
    while True:
        # Check if there's data available in the buffer
        if ser.in_waiting > 0:
            # Read the data from the serial buffer
            data = ser.readline().decode('utf-8').strip()  # Read line and decode to string
            print(data)
        else:
            # No data available, sleep for a short period to prevent high CPU usage
            time.sleep(0.1)  # Sleep for 100ms
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()  # Close the serial connection when done

