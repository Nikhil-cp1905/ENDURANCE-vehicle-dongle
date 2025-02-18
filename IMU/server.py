from flask import Flask, jsonify
import json
import serial
import time

app = Flask(__name__)

# Initialize serial port (replace with the correct port for your system)
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

# List to store data
data_list = []

# Route to fetch sensor data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data_list)


# Read and store data from Arduino
def read_data():
    global data_list
    try:
        while True:
            # Check if there's data available in the buffer
            if ser.in_waiting > 0:
                # Read the data from the serial buffer
                data = ser.readline().decode('utf-8').strip()  # Read line and decode to string
                if "Accel X:" in data:  # Only store valid sensor data
                    print(data)  # Optionally print to console
                    
                    # Create a dictionary for this data entry
                    data_entry = {
                        "data": data
                    }
                    
                    # Add the data entry to the list
                    data_list.append(data_entry)
                
                # Sleep for a short period to prevent high CPU usage
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting... Data stored")

if __name__ == '__main__':
    # Start the data reading process
    import threading
    data_thread = threading.Thread(target=read_data)
    data_thread.daemon = True
    data_thread.start()

    # Run the Flask app
    app.run(debug=True, host="0.0.0.0", port=5000)

