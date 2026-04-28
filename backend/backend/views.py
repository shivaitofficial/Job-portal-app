from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
@api_view(['GET'])
def hello_api(request):
    return Response({"message":"Hello From Django API"})

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User Registered successfully !"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def basic_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username=username,password=password)
        return Response({"message":"Login Sucessful"},status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message":"Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)


