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
    #select only one imge for the releated products
    productOneImge=[]
    imgesOfProduct=[]
    imegesForRelatedProducts = Image_Product.objects.all()
    for product_re in related_products :
        for img in imegesForRelatedProducts:
            if product_re.pk == img.product.pk:
                imgesOfProduct.append(img)
        if len(imgesOfProduct) >0:
            productOneImge.append(imgesOfProduct[0])
            imgesOfProduct=[]
    

    context = {
    'product': product,
    'imeges':imeges,
    'attributes':attribute,
    'attributeValue':attribute_value,
    'spacification':spacification,
    'categories':categories,
    'category':category,
    'related_products':related_products,
    'related_products_imeges':productOneImge
    }
    return render(request,"product-detail.html" , context)

#--------------------------------------------------------------------------------------
#desply all the products
def product_list(request):
    products =  Product.objects.all()
    categories= Category.objects.all()
    productOneImge=[]
    imgesOfProduct=[]
    imeges = Image_Product.objects.all()
    for product in products :
        for img in imeges:
            if product.pk == img.product.pk:
                imgesOfProduct.append(img)
        if len(imgesOfProduct) >0:
            productOneImge.append(imgesOfProduct[0])
            imgesOfProduct=[]
        
    context = {
    'products': products,
    'categories':categories,
    'imeges':productOneImge
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

    productOneImge=[]
    imgesOfProduct=[]
    imeges = Image_Product.objects.all()
    for product in products :
        for img in imeges:
            if product.pk == img.product.pk:
                imgesOfProduct.append(img)
        if len(imgesOfProduct) >0:
            productOneImge.append(imgesOfProduct[0])
            imgesOfProduct=[]
        
    context = {
    'products': products_filtered,
    'categories':categories,
    'imeges':productOneImge,
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

    productOneImge=[]
    imgesOfProduct=[]
    imeges = Image_Product.objects.all()
    for product in products :
        for img in imeges:
            if product.pk == img.product.pk:
                imgesOfProduct.append(img)
        if len(imgesOfProduct) >0:
            productOneImge.append(imgesOfProduct[0])
            imgesOfProduct=[]
        
    context = {
    'products': products_filtered,
    'categories':categories,
    'category':category,
    'imeges':productOneImge,
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
    productOneImge=[]
    imgesOfProduct=[]
    imeges = Image_Product.objects.all()
    for product in products :
        for img in imeges:
            if product.pk == img.product.pk:
                imgesOfProduct.append(img)
        if len(imgesOfProduct) >0:
            productOneImge.append(imgesOfProduct[0])
            imgesOfProduct=[]
        
    context = {
    'products': products,
    'category':category,
    'categories':categories,
    'imeges':productOneImge
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

# def change_password(request):
#     if request.method == "POST":
#         current_password = request.POST['current_password']
#         new_password = request.POST['new_password']
#         try:
#             u = User.objects.get(id=request.user.id)
#             if u.check_password(current_password):
#                 u.set_password(new_password)
#                 u.save()
#                 return render(request, "change_password.html")
#             else:
               
#                 return render(request, "change_password.html")
#         except:
#             pass
#     return render(request, "change_password.html")

