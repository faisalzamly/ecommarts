from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

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
@login_required(login_url = '/login')
def my_account(request):
    if request.method == "POST":
        if request.POST['current_password']!=None:
            current_password = request.POST['current_password']
            
            new_password = request.POST['new_password']
            confirm_password=request.POST['confirm_password']
            if new_password != confirm_password:
                passnotmatch = True
                return render(request, "my-account.html", {'passnotmatch':passnotmatch})
            try:
                u = User.objects.get(id=request.user.id)
                if u.check_password(current_password):
                    u.set_password(new_password)
                    u.save()
                    alert = True
                    return render(request, "my-account.html", {'alert':alert})
                else:
                    currpasswrong = True
                    return render(request, "my-account.html", {'currpasswrong':currpasswrong})
            except:
                pass
        else:
            pass
    else:
        return render(request, "my-account.html")
