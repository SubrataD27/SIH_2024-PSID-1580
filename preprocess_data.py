import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load collected data
data = pd.read_csv('sensor_data.csv')

# Normalize data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z']])

# Save the scaled data
pd.DataFrame(scaled_data, columns=['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z']).to_csv('scaled_sensor_data.csv', index=False)
