import smbus
import time
import csv

# Set up I2C communication
bus = smbus.SMBus(1)
mpu_address = 0x68

# Initialize MPU6050
bus.write_byte_data(mpu_address, 0x6B, 0)

def read_mpu6050():
    accel_x = bus.read_byte_data(mpu_address, 0x3B)
    accel_y = bus.read_byte_data(mpu_address, 0x3D)
    accel_z = bus.read_byte_data(mpu_address, 0x3F)
    gyro_x = bus.read_byte_data(mpu_address, 0x43)
    gyro_y = bus.read_byte_data(mpu_address, 0x45)
    gyro_z = bus.read_byte_data(mpu_address, 0x47)
    return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z

# Collect and save data
with open('sensor_data.csv', 'w') as file:
    writer = csv.writer(file,delimiter='|')
    data = ['timestamp', 'accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z']
    writer.writerow(data)

    try:
        while True:
            data = read_mpu6050()
            writer.writerow([time.time(), *data])
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Data collection stopped.")

