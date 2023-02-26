from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib.auth.models import User, Group



<<<<<<< HEAD
class ProfileInline(admin.StackedInline):
    model = Register_models
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username","password","first_name","last_name"]
    inlines = [ProfileInline]
=======

# class UserAdmin(admin.ModelAdmin):
#     model = User
#     fields = ["username","password","first_name","last_name"]

>>>>>>> 86c11700a4ae8db205e4836f92c93220deef9430

# admin.site.unregister(User)

<<<<<<< HEAD
admin.site.register(User,UserAdmin)
# admin.site.register(Register_models)
admin.site.register(Attribute)
=======
# admin.site.register(User,UserAdmin)
admin.site.register(Register_models)
>>>>>>> 86c11700a4ae8db205e4836f92c93220deef9430
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Attribute)
# admin.site.register(Attribute_Value)
admin.site.register(Attribute_product)
admin.site.register(Specification_Product)
admin.site.register(Image_Product)

