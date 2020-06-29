from rest_framework import serializers
from api.models import *
# 定义序列化器类 跟模型moles对应的
from drf_day1 import settings

# 定义序列化器类 跟模型moles对应的
class EmployeeSerializer(serializers.Serializer):
    """
    需要为每一个model编写一个单独的序列化器类
    """
    username = serializers.CharField()
    password = serializers.CharField()
    gender = serializers.IntegerField()
    # pic = serializers.ImageField()

    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        # print(obj.pic)
        # http://127.0.0.1:8000/media/pic/000.jpg
        # print("http://127.0.0.1:8000"+settings.MEDIA_URL + str(obj.pic))

        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))


# 反序列化
class EmployeeDeSerializer(serializers.Serializer):
    """
    反序列化：将前台提交的数据保存入库
    1. 前台需要提供哪些字段
    2. 对字段进行安全校验
    3. 哪些字段需要额外的校验
    """
    # 添加反序列化校验规则
    username = serializers.CharField(
        max_length=8,
        min_length=2,
        error_messages={
            "max_length": "长度太长了",
            "min_length": "长度太短了",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()

    # 想要完成新增员工  必须重写create()方法
    # 继承的serializer类并没有新增做具体的实现
    def create(self, validated_data):
        # 方法中完成新增
        print(validated_data)
        return Employee.objects.create(**validated_data)