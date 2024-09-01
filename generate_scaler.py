# generate_scaler.py
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

# Example training data (replace with your actual data)
training_data = np.array([
    [0.1, 0.2, 0.3, 0.4],
    [0.2, 0.3, 0.4, 0.5],
    # Add more data as needed
])

# Create and fit the scaler
scaler = StandardScaler()
scaler.fit(training_data)

# Save the scaler
joblib.dump(scaler, 'scaler.pkl')

print("Scaler saved as scaler.pkl")