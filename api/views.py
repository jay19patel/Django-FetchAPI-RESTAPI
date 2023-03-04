from django.shortcuts import render
from api.models import *
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.serializers import StudentSerializer

# get all data 
@api_view(['GET'])
def API_Page(request):
    std = Student.objects.all()
    serializer = StudentSerializer(std,many=True)
    print(serializer.data)
    return Response({'status':200,'payload':serializer.data,'message':'Recive All Data'}) 


# get data 
@api_view(['GET'])
def getapi(request,id):
    std = Student.objects.get(id=id)
    serializer = StudentSerializer(instance=std)
    print(serializer.data)
    return Response({'status':200,'payload':serializer.data,'message':'Recive One  Data'}) 



# send data 
@api_view(['POST'])
def addapi(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)
    # validation error display here 
    if not serializer.is_valid():
        return Response({'status':403,'error':serializer.errors,'message':'some thing wrong'})
    else:
        serializer.save()
    # print(data)
    return Response({'status':200,'payload':data,'message':'you send'})

# update data 
@api_view(['POST'])
def updateapi(request,id):
    std = Student.objects.get(id=id)
    serializer = StudentSerializer(instance=std, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({'status':403,'error':serializer.errors,'message':'some thing wrong'})
    # print(serializer.data)
    return Response({'status':200,'payload':serializer.data,'message':'Update api '}) 



# delete data 
@api_view(['DELETE'])
def deleteapi(request,id):
    std = Student.objects.get(id=id)
    std.delete()
    return Response({'status':200,'message':'delete api '}) 