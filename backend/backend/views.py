from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from .models import Job,Application
from .serializers import JobSerializer
from .serializers import ApplicationSerializer

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


@api_view(['GET'])
def job_list(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs,many=True)
    return  Response(serializer.data)


@api_view(['POST'])
def apply_job(request):
    job_id = request.data.get("job")
    applicant_id = request.data.get("applicant")

    # 🔴 Check duplicate
    if Application.objects.filter(job_id=job_id, applicant_id=applicant_id).exists():
        return Response(
            {"message": "You have already applied for this job"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ApplicationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Application submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
