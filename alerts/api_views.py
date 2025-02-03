from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlertSerializer

@api_view(['POST'])
def send_alert(request):
    serializer = AlertSerializer(data=request.data)
    if serializer.is_valid():
        # Handle the alert data (e.g., save to database, send to mobile app)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
