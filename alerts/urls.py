from django.urls import path
from .views import send_alert

urlpatterns = [
    path('send_alert/', send_alert, name='send_alert'),
    path('send_alert/', send_alert, name='send_alert_api'),
]
