from django.http import HttpResponse
from django.shortcuts import render
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


def index(request):

    prods = None
    c_id = request.GET.get('category')
    if c_id:
        prods = Product.ge_all_prod_by_id(c_id)
    else:
        prods = Product.ge_all_prod()

    cat = Category.ge_all_cat()
    return render(request, 'index.html', {'prds': prods, 'cat': cat})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        c = Customer(first_name=fname, last_name=lname, phone=phone, email=email, password=password)

        c.register()

        return HttpResponse("SUCCESS")
