from rest_framework import serializers, exceptions

from api1.models import Book, Press


class PressModelSerializer(serializers.ModelSerializer):
    """
    出版社的序列化器
    """

    class Meta:
        # 指定序列化的模型
        model = Press
        # 指定要序列化的字段
        fields = ("press_name", "address", "pic")


class BookModelSerializer(serializers.ModelSerializer):
    # 为序列化器自定以字段 (不推荐)
    # aaa = serializers.SerializerMethodField()
    #
    # def get_aaa(self, obj):
    #     return "aaa"

    # TODO 自定义连表查询  查询图书时将图书对应的出版的信息完整的查询出来
    # 可以在序列化器中嵌套另一个序列化器来完成多表查询
    # 需要与图书表的中外键名保持一致  在连表查询较多字段时推荐使用
    publish = PressModelSerializer()

    class Meta:
        # 指定当前序列化器要序列化的模型
        model = Book
        # 指定你要序列化模型的字段
        # fields = ("book_name", "price", "pic", "publish_name", "press_address", "author_list", "publish")
        fields = ("book_name", "price", "pic", "publish")

        # 可以直接查询所有字段
        # fields = "__all__"

        # 可以指定不展示哪些字段
        # exclude = ("is_delete", "create_time", "status")

        # 指定查询深度  关联对象的查询  可以查询出有外键关系的信息
        # depth = 1


class BookDeModelSerializer(serializers.ModelSerializer):
    """
    反序列器  数据入库使用
    """

    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors")

        # 添加DRF所提供的校验规
        extra_kwargs = {
            "book_name": {
                "required": True,  # 设置为必填字段
                "min_length": 3,  # 最小长度
                "error_messages": {
                    "required": "图书名是必填的",
                    "min_length": "长度不够，太短啦~"
                }
            },
            "price": {
                "max_digits": 5,
                "decimal_places": 4,
            }
        }

    def validate_book_name(self, value):
        # 自定义用户名校验规则
        if "1" in value:
            raise exceptions.ValidationError("图书名含有敏感字")
        return value

    # 全局校验钩子  可以通过attrs获取到前台发送的所有的参数
    def validate(self, attrs):
        # 可以对前端发送的所有数据进行自定义校验
        # print(self, "当前实例所使用的反序列化器")
        pwd = attrs.get("password")
        re_pwd = attrs.pop("re_pwd")
        # 自定义规则  两次密码如果不一致  则无法保存
        if pwd != re_pwd:
            raise exceptions.ValidationError("两次密码不一致")

        return attrs


class BookModelSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields应该填写哪些字段  应该填写序列化与反序列化字段的并集
        fields = ("book_name", "price", "publish", "authors", "pic")

        # 添加DRF所提供的校验规则
        # 通过此参数指定哪些字段是参与序列化的  哪些字段是参与反序列化的
        extra_kwargs = {
            "book_name": {
                "required": True,  # 设置为必填字段
                "min_length": 3,  # 最小长度
                "error_messages": {
                    "required": "图书名是必填的",
                    "min_length": "长度不够，太短啦~"
                }
            },
            # 指定此字段只参与反序列化
            "publish": {
                "write_only": True
            },
            "authors": {
                "write_only": True
            },
            # 指定某个字段只参与序列化
            "pic": {
                "read_only": True
            }
        }

    def validate_book_name(self, value):
        # 自定义用户名校验规则
        if "1" in value:
            raise exceptions.ValidationError("图书名含有敏感字")
        return value

    # 全局校验钩子  可以通过attrs获取到前台发送的所有的参数
    def validate(self, attrs):

        price = attrs.get("price", 0)
        # 没有获取到 price  所以是 NoneType
        if price > 90:
            raise exceptions.ValidationError("超过设定的最高价钱~")

        return attrs
