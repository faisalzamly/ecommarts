from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

        path("", index, name="index"),
        path("register/", register, name="register"),
        path("login/", login1, name="login"),
        path("my_account/", my_account, name="my_account"),
        path("product/<int:Product_pk>", product_Details, name="product_Details"),

]  