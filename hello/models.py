from django.db import models
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.

class User(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
        (2, "other"),
    )

    username = models.CharField(max_length=80)
    password = models.CharField(max_length=64)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)

    class Meta:
        db_table = "bz_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username