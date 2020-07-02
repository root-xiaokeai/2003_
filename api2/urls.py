from django.urls import path
from api2 import views
app_nam='api2'
urlpatterns = [
    path("user/", views.UserAPIViewV2.as_view({"post": "login","get":"register"})),

    path("user/<str:id>/", views.UserAPIViewV2.as_view({"post": "login","get":"register"})),
]
