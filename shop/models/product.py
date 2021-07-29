from django.db import models
from .category import Category
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def ge_all_prod():
        return Product.objects.all()

    @staticmethod
    def ge_all_prod_by_id(c_id):
        if c_id:
            return Product.objects.filter(category=c_id)
        else:
            return Product.ge_all_prod()