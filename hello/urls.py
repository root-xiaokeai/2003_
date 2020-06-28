from django.contrib import admin
from django.urls import path
from hello import views
app_name = 'user'
urlpatterns = [
    path('apiv/<str:id>/',views.UserAPIView.as_view()),
]
