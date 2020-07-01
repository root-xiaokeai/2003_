from django.contrib import admin

# Register your models here.
from api1 import models

admin.site.register(models.Author)
admin.site.register(models.AuthorDetail)
admin.site.register(models.Press)
admin.site.register(models.Book)