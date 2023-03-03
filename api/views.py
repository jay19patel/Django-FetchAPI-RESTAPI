from django.shortcuts import render
from api.models import *
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.serializers import StudentSerializer
# get data 
@api_view(['GET'])
def API_Page(request):
    std = Student.objects.all()
    serializer = StudentSerializer(std,many=True)
    print(serializer.data)
    return Response({'status':200,'payload':serializer.data,'message':'you send'}) 

# send data 
@api_view(['POST'])
def addapi(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)
    
    # validation error display here 
    if not serializer.is_valid():
        return Response({'status':403,'error':serializer.errors,'message':'some thing wrong'})
    print(data)
    return Response({'status':200,'payload':data,'message':'you send'})