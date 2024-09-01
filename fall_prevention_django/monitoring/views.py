import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .model_utils import predict_fall_risk

@api_view(['POST'])
def predict_risk(request):
    """
    API endpoint to predict fall risk based on sensor data.
    Expects incoming data in JSON format with a 'sensor_data' field.
    """
    data = request.data.get('sensor_data')
    if data:
        # Convert incoming data to a list of floats
        try:
            data = [float(x) for x in data.split(',')]
        except ValueError:
            return Response({'error': 'Invalid data format'}, status=400)
        
        fall_risk, confidence = predict_fall_risk(data)
        return Response({'fall_risk': fall_risk, 'confidence': confidence})
    else:
        return Response({'error': 'No data provided'}, status=400)

def read_latest_sensor_data():
    """
    Reads the latest row from sensor_data.csv and returns the data as a dictionary.
    """
    try:
        df = pd.read_csv('path/to/sensor_data.csv')  # Update this path to your CSV file location
        if not df.empty:
            latest_data = df.iloc[-1]  # Get the latest row
            return {
                'accel_x': latest_data['accel_x'],
                'accel_y': latest_data['accel_y'],
                'accel_z': latest_data['accel_z'],
                'heart_rate': latest_data['heart_rate'],
                'gsr_value': latest_data['gsr_value'],
            }
    except FileNotFoundError:
        return {
            'accel_x': 0,
            'accel_y': 0,
            'accel_z': 0,
            'heart_rate': 0,
            'gsr_value': 0,
        }
    return {
        'accel_x': 0,
        'accel_y': 0,
        'accel_z': 0,
        'heart_rate': 0,
        'gsr_value': 0,
    }

def latest_sensor_data(request):
    """
    API endpoint to get the latest sensor data from the CSV file.
    """
    data = read_latest_sensor_data()
    return JsonResponse(data)

def dashboard(request):
    """
    Renders the dashboard template.
    """
    return render(request, 'monitoring/dashboard.html')
