from django.shortcuts import render
from django.http import JsonResponse
from .models import Twerk

# Create your views here.
def index(request):
    if request.method=='GET':
        data={'data':'maybe seventh august'}
        return JsonResponse(data=data)
def get_all(request):
    if request.method=="GET":
        all_data=Twerk.objects.all()
        result=[]
        for twerk in all_data:
            result.append({'name':twerk.twerk_name,'bday':twerk.twerk_birth,"numb":twerk.twerk_birth})
        return JsonResponse({'data':result})