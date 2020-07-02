from django.db import models

# Create your models here.
class User_api2(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = "user_api2"
