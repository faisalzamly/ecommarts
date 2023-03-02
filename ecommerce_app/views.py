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
    'tags':tags

    }
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



def home(request):
    categories= Category.objects.all()
    context = {
    'categories':categories,
    }
    return render(request ,"index.html" , context)


