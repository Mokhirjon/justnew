from .serializers import TwerkSerializers
from rest_framework.views import APIView
from .models import Twerk
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
# Create your views here.
class TwerkALLView(APIView):
    def get(self,request,*args,**kwargs):
        all_twerks=Twerk.objects.all()
        serializers=TwerkSerializers(all_twerks,many=True)
        return Response(serializers.data)

class DetailTwerksView(APIView):
    def get(self, request, *args, **kwargs):
        twerks_id=kwargs['twerks_id']
        twerk= get_object_or_404(Twerk,id=twerks_id)
        serializer =TwerkSerializers(twerk)
        return Response(serializer.data)

class CreateTwerkView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = TwerkSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors)
class UpdateTWerksView(APIView):
    def put(self,request,*args,**kwargs):
        twerk= get_object_or_404(Twerk,id=kwargs['twerk_id'])
        serializers=TwerkSerializers(twerk,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
class DeleteTwerksView(APIView):
    def __delete__(self,request,*args,**kwargs):
        twerk= get_object_or_404(Twerk,id=kwargs['twerk_id'])
        twerk.delete()
        return Response({'msg':'deleted'})