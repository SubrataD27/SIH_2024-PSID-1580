import os
import numpy as np
import tensorflow as tf
import joblib

# Construct the paths to the model and scaler files
base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, 'fall_detection_model.h5')  # Ensure this matches your file name
scaler_path = os.path.join(base_dir, 'scaler.pkl')

# Load the trained model and scaler
model = tf.keras.models.load_model(model_path)
scaler = joblib.load(scaler_path)

def predict_fall_risk(data):
    """
    Predict the fall risk based on input data.

    Args:
        data (list or numpy array): Input data for prediction.

    Returns:
        tuple: Fall risk ('High' or 'Low') and prediction value (float).
    """
    # Ensure data is in the correct format
    if isinstance(data, list):
        data = np.array(data)
    
    # Preprocess the data
    data_scaled = scaler.transform([data])
    
    # Make predictions
    prediction = model.predict(data_scaled)
    
    # Interpret the predictions
    fall_risk = 'High' if prediction[0] > 0.5 else 'Low'
    
    return fall_risk, float(prediction[0])

# Example usage
if __name__ == "__main__":
    # Example input, replace with actual data
    data = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])  # Ensure this matches your input feature size
    fall_risk, prediction_value = predict_fall_risk(data)
    print(f"Fall Risk: {fall_risk}, Prediction Value: {prediction_value}")
