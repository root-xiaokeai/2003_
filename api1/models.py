from django.db import models
# Create your models here.
# python manage.py makemigrations
# python manage.py migrate

# 抽象表 基表
class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        # 在元数据中一旦声明此属性后  不会在数据库中创建对应的表结构
        # 其他模型继承这个模型后  可以继承表中的字段
        abstract = True

class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pic = models.ImageField(upload_to="pic", default="pic/1.jpeg")
    publish = models.ForeignKey(to="Press",  # 关联表
                                on_delete=models.CASCADE,  # 级联删除
                                db_constraint=False,  # 删除后对应字段的值可以为空
                                related_name="books")  # 反向查询的名称
    authors = models.ManyToManyField(to="Author", db_constraint=False, related_name="books")

    class Meta:
        db_table = "bz_book"
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name

class Press(BaseModel):
    press_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to="img", default="img/1.jpeg")
    address = models.CharField(max_length=256)

    class Meta:
        db_table = "bz_press"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.press_name


class Author(BaseModel):
    author_name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = "bz_author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name


class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=11)
    author = models.OneToOneField(to="Author", on_delete=models.CASCADE, related_name="detail")

    class Meta:
        db_table = "bz_author_detail"
        verbose_name = "作者详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s的详情" % self.author.author_name