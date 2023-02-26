from .views import *
from django.urls import path


urlpatterns = [

        path("", index, name="index"),
        path("register/", register, name="register"),
        path("login/", login1, name="login"),
        path("my_account/", my_account, name="my_account"),

]