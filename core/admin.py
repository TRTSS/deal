from django.contrib import admin
from core.models import BlogPost, Product, ProductPhoto, Order, SupportRequest, ProductTag


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id', 'user', 'creation_date']


# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Product)
admin.site.register(ProductPhoto)
admin.site.register(Order, OrderAdmin)
admin.site.register(SupportRequest)
admin.site.register(ProductTag)
