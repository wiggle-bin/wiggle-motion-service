import time
import board
import busio
import adafruit_adxl34x

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADXL345 accelerometer
accelerometer = adafruit_adxl34x.ADXL345(i2c)

try:
    while True:
        # Read acceleration data
        x, y, z = accelerometer.acceleration

        # Output the acceleration values
        print("X-axis: {:.2f}   Y-axis: {:.2f}   Z-axis: {:.2f}".format(x, y, z))

        # Wait for a short time before reading again
        time.sleep(0.1)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    pass
