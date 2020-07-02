from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin,DestroyModelMixin
from rest_framework import generics
from api2.serializers import *
from rest_framework import viewsets
from api2.models import *
# Create your views here.
from utils.response import APIResponse

class UserAPIViewV2(viewsets.ModelViewSet):
    serializer_class = UserDeModelSerializer
    def login(self,request,*args,**kwargs):
        try:
            username=request.data.get('username')
            password=request.data.get('password')
            user=User_api2.objects.get(username=username,password=password)
            user=UserDeModelSerializer(user).data
            return APIResponse(200,'登录成功',results=user)
        except:
            return APIResponse(500,"登录失败")
    def register(self,request,*args,**kwargs):
        try:
            response = self.create(request, *args, **kwargs)
            return APIResponse(200,'注册成功',results=response.data)
        except:
            return APIResponse(500,'注册失败')