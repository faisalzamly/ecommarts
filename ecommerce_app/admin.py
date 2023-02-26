from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib.auth.models import User




# class UserAdmin(admin.ModelAdmin):
#     model = User
#     fields = ["username","password","first_name","last_name"]


# admin.site.unregister(User)

# admin.site.register(User,UserAdmin)
admin.site.register(Register_models)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(Attribute_Value)
admin.site.register(Attribute_product)
admin.site.register(Image_Product)
admin.site.register(Specification_Product)

