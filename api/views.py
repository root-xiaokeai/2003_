from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import *


class User(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        print(id)
        if id:
            user=Employee.objects.get(pk=id)
            user=EmployeeSerializer(user).data
            return Response({
                    "status": 200,
                    "msg": "查询单个员工成功",
                    "results": user,
                })
        else:
            user=Employee.objects.all()
            user=EmployeeSerializer(user,many=True).data
            return Response({
                "status": 200,
                "msg": "查询单个员工成功",
                "results": user,
            })


    def post(self, request, *args, **kwargs):
        user=request.data
        # TODO 前端发送的数据需要入库时  必须对前台的数据进行校验
        if not isinstance(user, dict) or user == {}:
            return Response({
                "status": 501,
                "msg": "数据有误",
            })
        # 使用序列化器对前台提交的数据进行反序列化
        # 在反序列化时需要指定关键字参数  data
        serializer = EmployeeDeSerializer(data=user)
        # 对序列化的数据进行校验  通过is_valid() 方法对传递过来的参数进行校验  校验合法返回True
        if serializer.is_valid():
            # 调用save()去保存对象  必须重写create()方法
            emp_obj = serializer.save()
            print(emp_obj, "this is obj", type(emp_obj))
            # 将创建成功的用户实例返回到前端
            return Response({
                "status": 201,
                "msg": "用户创建成功",
                "results": EmployeeSerializer(emp_obj).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                # 验证失败后错误信息包含在 .errors中
                "results": serializer.errors
            })
