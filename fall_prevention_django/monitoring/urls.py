from django.contrib import admin
from django.urls import path
from monitoring.views import dashboard, predict_risk, latest_sensor_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('predict-risk/', predict_risk, name='predict_risk'),
    path('sensors/latest_data/', latest_sensor_data, name='latest_sensor_data'),
    # Add a root URL pattern
    path('', dashboard, name='home'),  # Redirect root URL to dashboard view
]
