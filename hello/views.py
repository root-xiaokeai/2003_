from django.shortcuts import render
# Create your views here.
from hello.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# 开发基于drf的视图
class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            user=User.objects.filter(id=id).values('username','password','gender').first()
            return Response({
                "status": 200,
                "message": "查询单个成功",
                "results": user
            })
        else:
            user=User.objects.all().values('username','password','gender')
            return Response({
                "status": 200,
                "message": "查询所有成功",
                "results": list(user)
            }
            )
        return Response({
            "status": 500,
            "message": "查询失败",
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user_obj = User.objects.create(username=username,password=password)
            if user_obj:
                return Response({
                    "status":200,
                    "message":"drf添加用户成功",
                    "results":{
                        "username":user_obj.username,
                        "password":user_obj.password,
                        "sex":user_obj.sex
                    }
                })
        except:
            return Response({
                "status":500,
                "message":"drf添加用户失败"
            })

    def put(self,request,*args, **kwargs):

        return Response('PUT GET SUCCESS')

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        if user_id:
            User.objects.filter(pk=user_id).first().delete()
            return Response({
                "status": 200,
                "message": "删除用户成功"
            })
        return Response({
            "status": 500,
            "message": "删除用户失败"
        })