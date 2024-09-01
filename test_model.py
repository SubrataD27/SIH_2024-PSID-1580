import numpy as np
import tensorflow as tf
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = tf.keras.models.load_model('fall_prevention_model.h5')

# Load the scaler used for training (if you used one)
scaler = joblib.load('scaler.pkl')

# Example input data (replace with actual test data)
test_data = np.array([
    [0.1, -0.2, 9.8, 0.01, 0.02, 0.03],  # Example data point 1
    [0.2, -0.1, 9.7, 0.02, 0.03, 0.04],  # Example data point 2
])

# Preprocess the data (scaling, etc.)
test_data_scaled = scaler.transform(test_data)

# Make predictions
predictions = model.predict(test_data_scaled)

# Interpret the predictions
for i, prediction in enumerate(predictions):
    fall_risk = 'High' if prediction[0] > 0.5 else 'Low'
    print(f"Test data point {i+1}: Fall risk is {fall_risk} (confidence: {prediction[0]:.2f}