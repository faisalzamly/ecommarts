from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        first_name=request.POST['first_Name']
        last_Name=request.POST['last_Name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        Password=request.POST['Password']
        confirm_password=request.POST['confirm_password']

        if Password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})
        if User.objects.filter(username=email):
            return render(request, "register.html")
        else:
            user =User.objects.create_user(username=email,first_name=first_name,last_name=last_Name,password=Password)
            register_models =Register_models.objects.create(user=user,mobile=mobile)
            user.save()
            register_models.save()
            return redirect ("/")
            # return render(request, "register.html")
    return render(request, "register.html")

def login1(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect ("/")
        return redirect ("/login")
    return render(request, "login.html")
    