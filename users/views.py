from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from users.models import *
from users.serializers import *  


class GetStudentView(APIView):    
    def get(self,request):
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name:
            instance =Student.objects.filter(firstname=name)
        else:
            instance = Student.objects.all()
        
        serializers= CreatedBySerializers(instance,many=True)
        return Response(data=serializers.data)
    def post(self,request):
        params = request.data
        print("params",params)
        serializers = CreatedBySerializers(data=params)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message","Done"})
class GetOrdersView(APIView): 
    def get(self,request):
        print("req",request.GET)
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name:
            instance =Orders.objects.filter(firstname=name)
        else:
            instance = Orders.objects.all()
        
        serializers= CreatedBySerializers(instance,many=True)
        return Response(data=serializers.data)
    def post(self,request):
        params = request.data
        print("params",params)
        serializers = CreatedBySerializers(data=params)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message","Done"})