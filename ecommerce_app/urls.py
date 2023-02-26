from .views import *
from django.urls import path


urlpatterns = [

        path("", index, name="index"),
        path("register/", register, name="register"),
        path("login/", login1, name="login"),

]