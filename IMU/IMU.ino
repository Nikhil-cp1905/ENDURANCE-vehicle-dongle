#include <Wire.h>
#include <Adafruit_MPU6050.h>

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200); // Start serial communication at 115200 baud rate
  Wire.begin();         // Initialize I2C communication

  // Initialize MPU6050
  Serial.println("Initializing MPU6050...");
  if (!mpu.begin()) {
    Serial.println("MPU6050 connection failed");
    while (1); // Halt if connection fails
  }
  Serial.println("MPU6050 connection successful");
}

void loop() {
  // Variables to store raw data
  sensors_event_t a, g, temp;

  // Read accelerometer and gyroscope data
  mpu.getEvent(&a, &g, &temp);

  // Print accelerometer data
  Serial.print("Accel X: "); Serial.print(a.acceleration.x);
  Serial.print(" | Accel Y: "); Serial.print(a.acceleration.y);
  Serial.print(" | Accel Z: "); Serial.println(a.acceleration.z);

  // Print gyroscope data
  Serial.print("Gyro X: "); Serial.print(g.gyro.x);
  Serial.print(" | Gyro Y: "); Serial.print(g.gyro.y);
  Serial.print(" | Gyro Z: "); Serial.println(g.gyro.z);

  Serial.println("--------------------------------------");

  delay(500); // Delay for readability
}
