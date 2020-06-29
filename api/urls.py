from django.contrib import admin
from django.urls import path
from api import views
app_name = 'api'
urlpatterns = [
    path('user/',views.User.as_view()),
    path('user/<str:id>/',views.User.as_view())
]
