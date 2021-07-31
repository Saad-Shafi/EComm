from django.contrib import admin
from .models import product, category, customer
# Register your models here.


#TO SHOW VIEW
class ViewProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class ViewCategory(admin.ModelAdmin):
    list_display = ['name']

class ViewCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'password', 'phone']

admin.site.register(product.Product, ViewProduct)
admin.site.register(category.Category, ViewCategory)
admin.site.register(customer.Customer, ViewCustomer)
