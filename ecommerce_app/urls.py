from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

        path("", home, name="home"),
        path("register/", register, name="register"),
        path("login/", login1, name="login"),
        path("my_account/", my_account, name="my_account"),
        path("product/<int:Product_pk>", product_Details, name="product_Details"),
        path("products", product_list, name="product_list"),
        path("products/category/<int:category_pk>", product_category, name="product_category"),
        path("Home", home, name="home"),
        path("products/price/<int:price_cat>", product_list_price, name="product_list_price"),
        path("products/category/<int:category_pk>/price/<int:price_cat>",
              product_list_priceAndCategory,
                name="product_list_priceAndCategory"),

]  