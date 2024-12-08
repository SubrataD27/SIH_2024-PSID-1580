# **Fall Prediction and Prevention System**
A wearable, sensor-based solution integrated with Artificial Intelligence (AI) for real-time fall prediction and prevention in elderly individuals. The device provides tactile, auditory, and visual feedback and alerts caregivers or emergency services with real-time notifications.

---

## **Developed By**
**Team Subraaj**  
**Team Leader:** Subrata Dhibar

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Components](#components)
4. [Setup Instructions](#setup-instructions)
5. [Hardware Integration](#hardware-integration)
6. [Software Integration](#software-integration)
7. [AI Model Training](#ai-model-training)
8. [Mobile Application Setup](#mobile-application-setup)
9. [Testing and Validation](#testing-and-validation)
10. [Future Enhancements](#future-enhancements)

---

## **Introduction**
Falls are a leading cause of injury and hospitalization among elderly individuals. This system uses multiple sensors to detect potential fall risks by analyzing the Line of Gravity (LOG) relative to the Base of Support (BOS). The device predicts falls using an AI model trained on sensor data and sends immediate alerts to caregivers via a mobile application.

---

## **Features**
- Real-time fall detection and prediction.
- Integrated with multiple sensors: MPU6050 (gyroscope, accelerometer), FSR 402 (pressure sensor), MAX30100 (heart rate and SpO2), and GSR (anxiety detection).
- Wearable design for ease of use.
- Audio alerts, visual notifications, and emergency message delivery.
- Mobile app integration for live monitoring and notifications.

---

## **Components**
### **Hardware**
1. Raspberry Pi 4 Model B
2. Arduino Uno
3. MPU6050 (Accelerometer & Gyroscope)
4. FSR 402 (Force Sensor)
5. MAX30100 (Heart Rate & SpO2 Sensor)
6. GSR Sensor (Galvanic Skin Response)
7. Rechargeable battery and power bank
8. Belt for wearable design

### **Software**
1. Arduino IDE
2. Python for Raspberry Pi
3. XGBoost for AI model training
4. Django framework for web-based monitoring
5. Firebase or MQTT for real-time communication
6. Mobile application (Android/iOS)

---

## **Setup Instructions**
### 1. **Hardware Assembly**
- Mount sensors securely onto the wearable belt.
- Connect the sensors to the Arduino as per the provided schematic.
- Connect the Arduino to the Raspberry Pi for digital data transfer.

### 2. **Software Setup**
#### Raspberry Pi:
- Install Raspbian OS on the Raspberry Pi.
- Set up necessary libraries (e.g., `pandas`, `numpy`, `scikit-learn`, `xgboost`).
- Install MQTT broker (e.g., Mosquitto) for real-time communication.

#### Arduino:
- Install Arduino IDE and configure it to detect the connected Arduino.
- Upload the sensor data acquisition code.

#### Mobile App:
- Configure Firebase for notification services.
- Set up WebSocket for real-time monitoring.

---

## **Hardware Integration**
1. **Arduino Connections**:
   - MPU6050: Connect to I2C pins.
   - FSR 402: Connect to analog input pins.
   - MAX30100: Connect via I2C pins.
   - GSR: Connect to analog input pins.
2. **Raspberry Pi**:
   - Connect Raspberry Pi to Arduino via USB.
   - Configure GPIO pins for additional sensor data if needed.

---

## **Software Integration**
1. **Sensor Data Acquisition**:
   - Use Arduino to read data from all sensors.
   - Send sensor data to Raspberry Pi for processing.

2. **AI Model**:
   - Train the XGBoost model with labeled datasets for fall detection.
   - Save the trained model as `.pkl` and load it on Raspberry Pi.

3. **Django Interface**:
   - Develop a web interface to visualize real-time sensor data and fall risks.
   - Integrate with Firebase or MQTT for sending alerts.

---

## **AI Model Training**
1. Collect sensor data under various conditions (normal activities, near falls, and actual falls).
2. Preprocess the data (cleaning, normalization).
3. Split the data into training and testing sets.
4. Train an XGBoost model to classify fall risks.
5. Validate the model with real-world test data to ensure accuracy.

---

## **Mobile Application Setup**
1. Build a mobile app using Flutter or Android Studio.
2. Set up Firebase Cloud Messaging for alert notifications.
3. Use Google Maps API to send the location during emergencies.
4. Enable live monitoring using WebSocket or MQTT.

---

## **Testing and Validation**
- Test the device with real-world activities to ensure accuracy.
- Validate the AI model's predictions.
- Perform stress testing for reliable mobile app notifications.

---

## **Future Enhancements**
- Add GPS tracking for location monitoring.
- Introduce predictive analytics for long-term fall risk assessment.
- Miniaturize the hardware for better portability.
- Develop a cloud-based dashboard for advanced data visualization.

---


---
