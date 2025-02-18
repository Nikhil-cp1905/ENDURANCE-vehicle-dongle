import serial
import time

# Specify the correct serial port and baud rate
# Replace '/dev/ttyUSB0' with the correct port for your system
ser = serial.Serial('/dev/ttyUSB0', 115200)  # Update with your port
time.sleep(2)  # Wait for Arduino to reset

# Read and print data from the Arduino
try:
    while True:
        # Read the data from the serial buffer
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()  # Read line and decode to string
            print(data)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()  # Close the serial connection when done

