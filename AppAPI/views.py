from django.shortcuts import render
from django.http import JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt


def homePage(request):
    context={}
    return render (request ,'Home.html',context)
#  ---------------------- fetch API -------------------
@csrf_exempt
def API(request):
    # recive data 
    json_data = json.loads(request.body)
    # message = json_data['name']
    print(json_data)

    # send data 
    # response_data = json_data 
    response_data = {"message": "recive data succesfully"}     
    return JsonResponse(response_data)

# ---------------------- fetch API -------------------


