from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

        path("", index, name="index"),
        path("register/", register, name="register"),
        path("login/", login1, name="login"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)