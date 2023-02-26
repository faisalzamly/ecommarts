from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib.auth.models import User, Group



class ProfileInline(admin.StackedInline):
    model = Register_models
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username","password","first_name","last_name"]
    inlines = [ProfileInline]

admin.site.unregister(User)

admin.site.register(User,UserAdmin)
# admin.site.register(Register_models)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Attribute_Value)
admin.site.register(Image_Product)
admin.site.register(Specification_Product)