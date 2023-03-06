from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

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
        username=request.POST['username']
        mobile=request.POST['mobile']
        Password=request.POST['Password']
        confirm_password=request.POST['confirm_password']

        if Password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})
        if User.objects.filter(username=username):
            return render(request, "register.html")
        else:
            user =User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_Name,password=Password)
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
      

        edit_user = Register_models.objects.get(user=request.user)
        first_name =request.POST['first_name']
        last_Name =request.POST['last_name']
        mobile =request.POST['mobile']
        email =request.POST['email']
        address =request.POST['address']
        edit_user.user.email = email
        edit_user.mobile = mobile
        edit_user.user.first_name = first_name
        edit_user.user.last_name = last_Name
        edit_user.address = address
        edit_user.user.save()
        edit_user.save()
        context = {
        'mobile':edit_user.mobile,
        'address':edit_user.address,
        }
        return render(request, "my-account.html",context)
        
                  
    else:
        edit_user = Register_models.objects.get(user=request.user)
        context = {
        'mobile':edit_user.mobile,
        'address':edit_user.address,
    }
        return render(request, "my-account.html",context)
@login_required(login_url = '/login')
def change_password(request):
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
        return render(request, "my-account.html", {'passnotmatch':passnotmatch})
#--------------------------------------------------------------------------------------
#product Details page
def product_Details(request , Product_pk):
    product = Product.objects.get(pk=Product_pk)
    imeges=Image_Product.objects.filter(product=product.pk)
    attribute=Attribute_product.objects.filter(product=product.pk)
    categories= Category.objects.all()
    category= Category.objects.get(pk=product.category.pk)
    related_products=Product.objects.filter(category=category.pk)
    attribute_value = []
    for att in attribute:
        attribute_value.append(att.attribute.name)
    MyAttributeset = set(attribute_value)
    attribute_value = list(MyAttributeset)

    spacification = Specification_Product.objects.filter(product=product.pk)
    prands = Prand.objects.all()
    tags=Tag_product.objects.filter(product=product.pk)
    products=Product.objects.all()
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in products:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)
    
    review = Review.objects.filter(product=product.pk)

    context = {
    'product': product,
    'imeges':imeges,
    'attributes':attribute,
    'attributeValue':attribute_value,
    'spacification':spacification,
    'categories':categories,
    'category':category,
    'related_products':related_products,
    'prands':prandinfo,
    'tags':tags,
    'review':review


    }
    if request.method == "POST":
        
        name=request.user.first_name
        email=request.user.email
        review=request.POST['review']
        review=Review.objects.create(name=name,email=email,review=review,product=product)
        review.save()
        return render(request,"index.html" )
    return render(request,"product-detail.html" , context)

#--------------------------------------------------------------------------------------
#desply all the products
def product_list(request):
    products =  Product.objects.all()
    categories= Category.objects.all()
    prands = Prand.objects.all()
    tags=Tags.objects.all()
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in products:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)
    context = {
    'products': products,
    'categories':categories,
    'prands':prandinfo,
    'tags':tags
    }
    return render(request ,"product-list.html" , context)

#--------------------------------------------------------------------------------------
#desply all the products with pagination
def product_list_pagination(request,page):
    products =  Product.objects.all()
    paginator = Paginator(products, per_page=9)
    page_object = paginator.get_page(page)
    categories= Category.objects.all()
    prands = Prand.objects.all()
    tags=Tags.objects.all()
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in products:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)

    has_pre=page_object.has_previous()
    has_next=page_object.has_next()
    pre=page_object.number-1
    next=page_object.number+1
    context = {
    'products': page_object,
    'categories':categories,
    'prands':prandinfo,
    'tags':tags,
    'page_num':page,
    'has_pre':has_pre,
    'has_next':has_next,
    'pre':pre,
    'next':next
    }
    return render(request ,"product-list.html" , context)
#--------------------------------------------------------------------------------------
#desply all the products with pagination API
def product_list_api(request):
    products =  Product.objects.all()
    categories= Category.objects.all()
    prands = Prand.objects.all()
    tags=Tags.objects.all()
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in products:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)
    context = {
    'products': products,
    'categories':categories,
    'prands':prandinfo,
    'tags':tags,
    }
    return render(request ,"product-list_api.html" , context)

def listing_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 9)
    keywords = Product.objects.all()
    paginator = Paginator(keywords, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"name": product.name , } for product in page_obj.object_list]
    payload = {
    "page": {
    "current": page_obj.number,
    "has_next": page_obj.has_next(),
    "has_previous": page_obj.has_previous(),
    },
    "data": data
    }
    return JsonResponse(payload)


#-----------------------------------------------------------
#Prand products
def product_prand_list(request,prand_pk):
    products =  Product.objects.filter(prand=prand_pk)
    categories= Category.objects.all()
    prands = Prand.objects.all()
    tags=Tags.objects.all()
    ProductsPrand=Prand.objects.get(pk=prand_pk)
    allProducts=Product.objects.all()
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in allProducts:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)
        
    
    context = {
    'products': products,
    'categories':categories,
    'tags':tags,
    'prands':prandinfo,
    'ProductsPrand':ProductsPrand
    }
    return render(request ,"product-list.html" , context)


#-----------------------------------------------------------
#Prand products
def product_tag_list(request,tag_pk):
    tags =  Tag_product.objects.all()
    tag=Tags.objects.get(pk=tag_pk)
    my_products=[]
    for item in tags:
        if item.tag.pk==tag_pk:
            prodct=Product.objects.get(pk=item.product.pk)
            my_products.append(prodct)
    categories= Category.objects.all()
    prands = Prand.objects.all()
    tags=Tags.objects.all()
    allProducts=Product.objects.all()
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in allProducts:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)
        
    
    context = {
    'products': my_products,
    'categories':categories,
    'tags':tags,
    'prands':prandinfo,
    'tag':tag,
    }
    return render(request ,"product-list.html" , context)



#-----------------------------------------------------------
#Categoty Prand products
def product_category_prand_list(request,category_pk, prand_pk):
    products =  Product.objects.filter(prand=prand_pk)
    categories= Category.objects.all()
    prands = Prand.objects.all()
    tags=Tags.objects.all()
    selected_products=[]
    ProductsPrand=Prand.objects.get(pk=prand_pk)
    for product in products:
        print('aaaa')
        if product.category.pk==category_pk:
            selected_products.append(product)
            print('sss')
    category= Category.objects.get(pk=category_pk)
    allProducts=Product.objects.filter(category=category_pk)
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in allProducts:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)
        
    
    context = {
    'products': selected_products,
    'categories':categories,
    'category':category,
    'tags':tags,
    'prands':prandinfo,
    'ProductsPrand':ProductsPrand
    }
    return render(request ,"product-list.html" , context)



#--------------------------------------------------------------------------------------
#filter the products based on it's price
def product_list_price(request,price_cat):
    products =  Product.objects.all()
    categories= Category.objects.all()
    products_filtered=[]
    max_price=0
    min_price=0
    price_text=''
    if price_cat==1:
        min_price=0
        max_price=50
        price_text='$0 to $50'
    elif price_cat==2:
        min_price=50
        max_price=100
        price_text='$50 to $100'
    elif price_cat==3:
        min_price=100
        max_price=150
        price_text='$100 to $150'
    elif price_cat==4:
        min_price=150
        max_price=200
        price_text='$150 to $200'
    elif price_cat==5:
        min_price=200
        max_price=250
        price_text='$200 to $250'
    elif price_cat==6:
        min_price=250
        max_price=300
        price_text='$250 to $300'
    elif price_cat==7:
        min_price=300
        max_price=350
        price_text='$300 to $350'
    elif price_cat==8:
        min_price=350
        max_price=400
        price_text='$350 to $400'
    elif price_cat==9:
        min_price=400
        max_price=450
        price_text='$400 to $450'
    elif price_cat==10:
        min_price=450
        max_price=3000
        price_text='$450 to $3000'

    for product in products:
        if int(product.price) >min_price and int(product.price)<=max_price:
            products_filtered.append(product)


        
    context = {
    'products': products_filtered,
    'categories':categories,
    'price_cat':price_cat,
    'price_text':price_text
    }
    return render(request ,"product-list.html" , context)


#--------------------------------------------------------------------------------------
#filter the products based on it's price and categores
def product_list_priceAndCategory(request,category_pk,price_cat):
    products =  Product.objects.filter(category=category_pk)
    category= Category.objects.get(pk=category_pk)
    categories= Category.objects.all()
    products_filtered=[]
    max_price=0
    min_price=0
    price_text=''
    if price_cat==1:
        min_price=0
        max_price=50
        price_text='$0 to $50'
    elif price_cat==2:
        min_price=50
        max_price=100
        price_text='$50 to $100'
    elif price_cat==3:
        min_price=100
        max_price=150
        price_text='$100 to $150'
    elif price_cat==4:
        min_price=150
        max_price=200
        price_text='$150 to $200'
    elif price_cat==5:
        min_price=200
        max_price=250
        price_text='$200 to $250'
    elif price_cat==6:
        min_price=250
        max_price=300
        price_text='$250 to $300'
    elif price_cat==7:
        min_price=300
        max_price=350
        price_text='$300 to $350'
    elif price_cat==8:
        min_price=350
        max_price=400
        price_text='$350 to $400'
    elif price_cat==9:
        min_price=400
        max_price=450
        price_text='$400 to $450'
    elif price_cat==10:
        min_price=450
        max_price=3000
        price_text='$450 to $3000'
 
    for product in products:
        if int(product.price) >min_price and int(product.price)<=max_price:
            products_filtered.append(product)

        
    context = {
    'products': products_filtered,
    'categories':categories,
    'category':category,
    'price_cat':price_cat,
    'price_text':price_text
    }
    return render(request ,"product-list.html" , context)



#--------------------------------------------------------------------------------------
#filter the products based on it's category
def product_category(request,category_pk):
    products =  Product.objects.filter(category=category_pk)
    category= Category.objects.get(pk=category_pk)
    categories= Category.objects.all()
    prands = Prand.objects.all()
    tags = Tags.objects.all()
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in products:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)
    context = {
    'products': products,
    'category':category,
    'categories':categories,
    'prands':prandinfo,
    'tags':tags,
    }
    return render(request ,"product-list.html" , context)



#--------------------------------------------------------------------------------------
#desply all the products
def orderd_product_list(request,order_cat):
    if order_cat==1:
        products =  Product.objects.all().order_by('-created_at')
        order_style='Newest'
    elif order_cat==2:
        products =  Product.objects.all().order_by('created_at')
        order_style='Oldest'
    else:
        Product.objects.all()
    categories= Category.objects.all()
    prands = Prand.objects.all()
    tags=Tags.objects.all()
    prandinfo=[]
    for pran in prands :
        count=0
        pranditem = {}
        for prducta in products:
            if(prducta.prand.pk==pran.pk):
                count+=1
        if count>0:
            pranditem.update({"name":pran})
            pranditem.update({"count":count})
            pranditem.update({"pk":pran.pk})
            prandinfo.append(pranditem)
    context = {
    'products': products,
    'categories':categories,
    'prands':prandinfo,
    'tags':tags,
    'order_style':order_style
    }
    return render(request ,"product-list.html" , context)



# Add Order in The Cart
def cart(request):

    if request.user.is_authenticated:
        user =request.user.id
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items":0, "get_cart_total":0}
    context = {
        "items": items,
        "order": order
    }
    return render(request, "cart.html", context)


# Create Checkout cart
def checkout(request):
    if request.user.is_authenticated:
        user =request.user.id
        order, created = Order.objects.get_or_create(user=user, complete=False) 
    else:
        order = {"get_cart_items":0, "get_cart_total":0}
    context = {
        "order": order
    }
    return render(request, "checkout.html", context)


# Billing Shipping Address
def shippingAddress(request):
    pass


# Home page
def home(request):
    categories= Category.objects.all()
    slider = Slider.objects.filter(active=True)[:4]
    context = {
    'categories':categories,
    'slider':slider
    }
    return render(request ,"index.html" , context)


def contact(request):
    if request.method == "POST":       
        subject=request.POST['subject']        
        message=request.POST['message']     
        data_user = Register_models.objects.get(user=request.user)
        email=data_user.user.email
        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
            )   
        Contact.objects.create(email=email,subject=subject,message=message)
        return render(request ,"contact.html")
    return render(request ,"contact.html")


def Logout(request):
    logout(request)
    return redirect ("/")