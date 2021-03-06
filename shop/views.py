from django.http import HttpResponse
from django.shortcuts import render, redirect
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

        #Validation can be added here

        c = Customer(first_name=fname, last_name=lname, phone=phone, email=email, password=password)

        isExist = c.isExist()
        isExCon = c.isExistCon()

        if isExist or isExCon:
            error = "User Already Exist"
            return render(request, 'signup.html', {'er': error})
        else:
            c.register()
            return redirect("index")


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('pass')

        c = Customer.getCustomer(email)
        if c:
            if password == c.password:
                request.session['customer'] = c.id
                return redirect("index")
            else:
                error = "Invalid Email or Password"
        else:
            print("Hello how are you")
            error = "Invalid Email or Password"

        return render(request, 'login.html', {'er': error})

def logout(request):
    request.session.clear()
    return redirect("index")


