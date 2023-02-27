from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib.auth.models import User, Group



<<<<<<< HEAD

=======
>>>>>>> 620e8d1fcf56fc737f44a2f026e0aff685b19800
class ProfileInline(admin.StackedInline):
    model = Register_models
class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]
<<<<<<< HEAD

=======
>>>>>>> 620e8d1fcf56fc737f44a2f026e0aff685b19800

admin.site.unregister(User)

<<<<<<< HEAD


# admin.site.unregister(User)


admin.site.register(User,UserAdmin)
# admin.site.register(Register_models)
admin.site.register(Attribute)

# admin.site.register(User,UserAdmin)
admin.site.register(Register_models)

=======
admin.site.register(User,UserAdmin)
admin.site.register(Register_models)
>>>>>>> 620e8d1fcf56fc737f44a2f026e0aff685b19800
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Attribute)
# admin.site.register(Attribute_Value)
admin.site.register(Attribute_product)
admin.site.register(Specification_Product)
admin.site.register(Image_Product)

